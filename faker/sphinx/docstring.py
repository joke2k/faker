# coding=utf-8
import re

from collections import OrderedDict  # noqa: F401 Do not remove! The eval command needs this reference.

from sphinx.util import logging

from faker import Faker
from faker.config import AVAILABLE_LOCALES, DEFAULT_LOCALE
from faker.sphinx.validator import SampleCodeValidator

logger = logging.getLogger(__name__)
_fake = Faker(AVAILABLE_LOCALES)
_base_provider_method_pattern = re.compile(r'^faker\.providers\.BaseProvider\.(?P<method>\w+)$')
_standard_provider_method_pattern = re.compile(r'^faker\.providers\.\w+\.Provider\.(?P<method>\w+)$')
_locale_provider_method_pattern = re.compile(
    r'^faker\.providers\.\w+'
    r'\.(?P<locale>[a-z]{2,3}_[A-Z]{2})'
    r'\.Provider'
    r'\.(?P<method>\w+)$',
)


class ProviderMethodDocstring:
    """
    Class that preprocesses provider method docstrings to generate sample usage and output

    Notes on how samples are generated:
    - If the docstring belongs to a standard provider method, sample usage and output will be
      generated using a `Faker` object in the `DEFAULT_LOCALE`.
    - If the docstring belongs to a localized provider method, the correct locale will be used.
    - If the docstring does not belong to any provider method, docstring preprocessing will be skipped.
    - The `Faker` objects used will be reseeded via `Faker.seed(0)` before each sample generation.
    """

    def __init__(self, app, what, name, obj, options, lines):
        self._line_iter = iter(lines)
        self._parsed_lines = []
        self._samples = []
        self._skipped = True

        if what != 'method':
            return

        base_provider_method_match = _base_provider_method_pattern.match(name)
        locale_provider_method_match = _locale_provider_method_pattern.match(name)
        standard_provider_method_match = _standard_provider_method_pattern.match(name)
        if base_provider_method_match:
            groupdict = base_provider_method_match.groupdict()
            self._method = groupdict['method']
            self._locale = DEFAULT_LOCALE
        elif standard_provider_method_match:
            groupdict = standard_provider_method_match.groupdict()
            self._method = groupdict['method']
            self._locale = DEFAULT_LOCALE
        elif locale_provider_method_match:
            groupdict = locale_provider_method_match.groupdict()
            self._method = groupdict['method']
            self._locale = groupdict['locale']
        else:
            return

        self._skipped = False
        self._parse()
        self._generate_samples()

    def _parse(self):
        while True:
            try:
                line = next(self._line_iter)
            except StopIteration:
                break
            else:
                self._process_section(line)
        self._kwargsify_samples()

    def _process_section(self, section):
        # No-op if section does not look like the start of a sample
        if not section.startswith(':sample: '):
            self._parsed_lines.append(section)
            return

        try:
            next_line = next(self._line_iter)
        except StopIteration:
            # No more lines left to consume, so save current sample section
            self._samples.append(section)
            return

        # Next line is the start of a new sample section,
        # so save current section, and start a new section
        if next_line.startswith(':sample: '):
            self._samples.append(section)
            self._process_section(next_line)

        # Next line is an empty line indicating the end of
        # current sample section, so save current section
        elif next_line == '':
            self._samples.append(section)

        # Section is assumed to be multiline, so continue
        # adding lines to current sample section
        else:
            section = section + ' ' + next_line
            self._process_section(section)

    def _kwargsify_samples(self):
        def _kwargsify_sample(text):
            def _repl(match):
                quoted = match.group(1) or match.group(2)
                return quoted if quoted else ' '
            return re.sub(r'("[^"]*")|(\'[^\']*\')|[ \t]+', _repl, text).replace(':sample: ', '').strip()

        for idx, sample_line in enumerate(self._samples):
            self._samples[idx] = _kwargsify_sample(sample_line)

    def _generate_samples(self):
        if not self._samples:
            return

        sample_section_output = ''
        generator = _fake[self._locale]
        for sample in self._samples:
            Faker.seed(0)
            if sample == 'default':
                result = generator.format(self._method)
                sample_output = '>>> fake.{method}()\n{result}\n'.format(
                    method=self._method, result=result,
                )
                sample_section_output += sample_output
            else:
                command = 'generator.{method}({kwargs})'.format(
                    method=self._method, kwargs=sample,
                )
                validator = SampleCodeValidator(command)
                if not validator.errors:
                    try:
                        result = eval(command)
                    except Exception:
                        msg = 'Sample generation failed for method `{method}` with arguments `{kwargs}`'.format(
                            method=self._method, kwargs=sample,
                        )
                        logger.warning(msg)
                    else:
                        sample_output = '>>> fake.{method}({kwargs})\n{result}\n'.format(
                            method=self._method, kwargs=sample, result=result,
                        )
                        sample_section_output += sample_output

        sample_section_output = ':examples:\n\n' + sample_section_output
        self._parsed_lines.extend(sample_section_output.split('\n'))

    @property
    def skipped(self):
        return self._skipped

    @property
    def lines(self):
        return self._parsed_lines
