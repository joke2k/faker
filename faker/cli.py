# coding=utf-8

from __future__ import unicode_literals
from __future__ import print_function

import os
import sys
import argparse

from faker import Faker, Factory, documentor
from faker import VERSION
from faker.config import AVAILABLE_LOCALES, DEFAULT_LOCALE, META_PROVIDERS_MODULES


if sys.version < '3':
    text_type = unicode
    binary_type = str
else:
    text_type = str
    binary_type = bytes


__author__ = 'joke2k'


def print_provider(doc, provider, formatters, excludes=None, output=None):
    output = output or sys.stdout
    if excludes is None:
        excludes = []

    print(file=output)
    print("### {0}".format(
          doc.get_provider_name(provider)), file=output)
    print(file=output)

    for signature, example in formatters.items():
        if signature in excludes:
            continue
        try:
            lines = text_type(example).expandtabs().splitlines()
        except UnicodeDecodeError:
            # The example is actually made of bytes.
            # We could coerce to bytes, but that would fail anyway when we wiil
            # try to `print` the line.
            lines = ["<bytes>"]
        except UnicodeEncodeError:
            raise Exception('error on "{0}" with value "{1}"'.format(
                            signature, example))
        margin = max(30, doc.max_name_len+1)
        remains = 150 - margin
        separator = '#'
        for line in lines:
            for i in range(0, (len(line) // remains) + 1):
                print("\t{fake:<{margin}}{separator} {example}".format(
                    fake=signature,
                    separator=separator,
                    example=line[i*remains:(i+1)*remains],
                    margin=margin
                ), file=output)
                signature = separator = ' '


def print_doc(provider_or_field=None,
              args=None, lang=DEFAULT_LOCALE, output=None, includes=None):
    args = args or []
    output = output or sys.stdout
    fake = Faker(locale=lang, includes=includes)

    from faker.providers import BaseProvider
    base_provider_formatters = [f for f in dir(BaseProvider)]

    if provider_or_field:
        if '.' in provider_or_field:
            parts = provider_or_field.split('.')
            locale = parts[-2] if parts[-2] in AVAILABLE_LOCALES else lang
            fake = Factory.create(locale, providers=[provider_or_field], includes=includes)
            doc = documentor.Documentor(fake)
            doc.already_generated = base_provider_formatters
            print_provider(
                doc,
                fake.get_providers()[0],
                doc.get_provider_formatters(fake.get_providers()[0]),
                output=output)
        else:
            try:
                print(fake.format(provider_or_field, *args), end='', file=output)
            except AttributeError:
                raise ValueError('No faker found for "{0}({1})"'.format(
                    provider_or_field, args))

    else:
        doc = documentor.Documentor(fake)

        formatters = doc.get_formatters(with_args=True, with_defaults=True)

        for provider, fakers in formatters:

            print_provider(doc, provider, fakers, output=output)

        for language in AVAILABLE_LOCALES:
            if language == lang:
                continue
            print(file=output)
            print('## LANGUAGE {0}'.format(language), file=output)
            fake = Faker(locale=language)
            d = documentor.Documentor(fake)

            for p, fs in d.get_formatters(with_args=True, with_defaults=True,
                                          locale=language,
                                          excludes=base_provider_formatters):
                print_provider(d, p, fs, output=output)


class Command(object):

    def __init__(self, argv=None):
        self.argv = argv or sys.argv[:]
        self.prog_name = os.path.basename(self.argv[0])

    def execute(self):
        """
        Given the command-line arguments, this creates a parser appropriate
        to that command, and runs it.
        """

        # retrieve default language from system environment
        default_locale = os.environ.get('LANG', 'en_US').split('.')[0]
        if default_locale not in AVAILABLE_LOCALES:
            default_locale = DEFAULT_LOCALE

        formatter_class = argparse.RawDescriptionHelpFormatter
        parser = argparse.ArgumentParser(
            prog=self.prog_name,
            description='{0} version {1}'.format(self.prog_name, VERSION),
            formatter_class=formatter_class)

        parser.add_argument("--version", action="version",
                            version="%(prog)s {0}".format(VERSION))

        parser.add_argument('-o', metavar="output",
                            type=argparse.FileType('w'),
                            default=sys.stdout,
                            help="redirect output to a file")

        parser.add_argument('-l', '--lang',
                            choices=AVAILABLE_LOCALES,
                            default=default_locale,
                            help="specify the language for a localized "
                            "provider (e.g. de_DE)")
        parser.add_argument('-r', '--repeat',
                            default=1,
                            type=int,
                            help="generate the specified number of outputs")
        parser.add_argument('-s', '--sep',
                            default='\n',
                            help="use the specified separator after each "
                            "output")

        parser.add_argument('-i',
                            '--include',
                            default=META_PROVIDERS_MODULES,
                            nargs='*',
                            help="list of additional custom providers to "
                            "user, given as the import path of the module "
                            "containing your Provider class (not the provider "
                            "class itself)")

        parser.add_argument('fake',
                            action='store',
                            nargs='?',
                            help="name of the fake to generate output for "
                                 "(e.g. profile)")

        parser.add_argument('fake_args',
                            metavar="fake argument",
                            action='store',
                            nargs='*',
                            help="optional arguments to pass to the fake "
                                 "(e.g. the profile fake takes an optional "
                                 "list of comma separated field names as the "
                                 "first argument)")

        arguments = parser.parse_args(self.argv[1:])

        for i in range(arguments.repeat):

            print_doc(arguments.fake,
                      arguments.fake_args,
                      lang=arguments.lang,
                      output=arguments.o,
                      includes=arguments.include
                      )
            print(arguments.sep, file=arguments.o)

            if not arguments.fake:
                # repeat not supported for all docs
                break


def execute_from_command_line(argv=None):
    """A simple method that runs a Command."""
    if sys.stdout.encoding is None:
        print('please set python env PYTHONIOENCODING=UTF-8, example: '
              'export PYTHONIOENCODING=UTF-8, when writing to stdout',
              file=sys.stderr)
        exit(1)

    command = Command(argv)
    command.execute()
