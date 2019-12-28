# coding=utf-8
from __future__ import unicode_literals
import re
import warnings

from faker import Faker
from faker.config import DEFAULT_LOCALE, AVAILABLE_LOCALES
from faker.sphinx.validator import SampleCodeValidator

fake = Faker(AVAILABLE_LOCALES)
base_provider_method_pattern = re.compile(r'^faker\.providers\.BaseProvider\.(?P<method>\w+)$')
provider_method_pattern = re.compile(r'^faker\.providers\.\w+\.Provider\.(?P<method>\w+)$')
locale_provider_method_pattern = re.compile(
    r'^faker\.providers\.\w+'
    r'\.(?P<locale>[a-z]{2,3}_[A-Z]{2})'
    r'\.Provider'
    r'\.(?P<method>\w+)$'
)

sample_pattern = re.compile(r':sample: (?P<signature>.*)$')


class ProviderMethodDocstring(object):

    def __init__(self, app, what, name, obj, options, lines):
        self._line_iter = iter(lines)
        self._parsed_lines = []
        self._sample_lines = []
        self._skipped = True

        if what != 'method':
            return

        base_provider_method_match = base_provider_method_pattern.match(name)
        locale_provider_method_match = locale_provider_method_pattern.match(name)
        provider_method_pattern_match = provider_method_pattern.match(name)
        if base_provider_method_match:
            groupdict = base_provider_method_match.groupdict()
            self._method = groupdict['method']
            self._locale = DEFAULT_LOCALE
        elif provider_method_pattern_match:
            groupdict = provider_method_pattern_match.groupdict()
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

    def _parse(self):
        while True:
            try:
                line = next(self._line_iter)
            except StopIteration:
                break
            else:
                self._process_line(line)
        self._generate_samples()

    def _process_line(self, line):
        if line.startswith(':sample: '):
            self._handle_sample_line(line)
        else:
            self._handle_noop_line(line)

    def _handle_noop_line(self, line):
        self._parsed_lines.append(line)

    def _handle_sample_line(self, line):
        next_line = next(self._line_iter)
        if next_line.startswith(':sample: '):
            self._sample_lines.append(line.replace(':sample: ', ''))
            self._handle_sample_line(next_line)
        elif next_line == '':
            self._sample_lines.append(line.replace(':sample: ', ''))
        else:
            line = line + ' ' + next_line
            self._handle_sample_line(line)

    def _generate_samples(self):
        if not self._sample_lines:
            return

        sample_section_output = ''
        generator = fake[self._locale]
        for sample in self._sample_lines:
            Faker.seed(0)
            sample = sample.strip()
            if sample == 'default':
                result = generator.format(self._method)
                sample_output = '>>> fake.{method}()\n{result}\n'.format(
                    method=self._method, result=result
                )
                sample_section_output += sample_output
            else:
                command = 'generator.{method}({kwargs})'.format(
                    method=self._method, kwargs=sample
                )
                validator = SampleCodeValidator(command)
                if not validator.errors:
                    try:
                        result = eval(command)
                    except Exception:
                        # TODO
                        warnings.warn('Something went wrong', RuntimeWarning)
                    else:
                        sample_output = '>>> fake.{method}({kwargs})\n{result}\n'.format(
                            method=self._method, kwargs=sample, result=result
                        )
                        sample_section_output += sample_output

        sample_section_output = ':examples:\n\n' + sample_section_output
        self._parsed_lines.extend(sample_section_output.split('\n'))

    @property
    def skipped(self):
        return self._skipped

    def lines(self):
        return self._parsed_lines
