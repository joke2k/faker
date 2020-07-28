from collections import OrderedDict
import json
import logging
import sys

from faker.factory import Factory

logger = logging.getLogger(__name__)


class Builder:
    """Data Structure builder"""

    def __init__(self,
                 locale: str = None,
                 providers: str = None,
                 generators: str = None,
                 includes: str = None,
                 **config):
        self._factory = Factory.create(locale, providers, generators, includes, **config)

    def csv(self, spec: list, rows: int, delimiter: str = "|", header: bool = False):
        """
        Returns a generator that will create CSV data as per the spec

        Specification Format
            [('label', 'provider', 'options')]

        :param spec: specification for the data structure
        :param rows: number of rows the generator will yield
        :param delimiter: delimiter used between fields
        :param header: first row returned is a header
        :return: generator
        """

        if header:
            yield delimiter.join([entry[0] for entry in spec])

        for _ in range(rows):
            row = self._create_entry(spec)
            yield delimiter.join(row.values())

    def fixed_width(self, spec: list, rows: int) -> iter:
        """
        Returns a generator that will create fixed width data as per the spec

        Specification Format
            [('char_width', 'provider', 'options')]

        :param spec: specification for the data structure
        :param rows: number of rows the generator will yield
        :return: generator
        """

        for _ in range(rows):
            entry = []
            for width, provider_name, *options in spec:
                params = options[0] if options else {}
                provider = getattr(self._factory, provider_name)
                result = provider(**params) if callable(provider) else ""
                field = "{0:<%s}" % width
                entry.append(field.format(result)[:width])
            yield ''.join(entry)

    def json(self, spec: list, rows: int, indent=None) -> iter:
        """
        Returns a generator that will create JSON data as per the spec

        Specification Format
            [('label', 'provider', 'options')]

        :param spec: specification for the data structure
        :param rows: number of rows the generator will yield
        :param indent: number of spaces to indent the fields
        :return: generator
        """

        for _ in range(rows):
            entry = self._create_entry(spec)
            yield json.dumps(entry, indent=indent)

    def json_block(self, spec: list, rows: int, indent=None) -> str:
        """
        Returns a serialized JSON list as per the spec

        Specification Format
            [('label', 'provider', 'options')]

        :param spec: specification for the data structure
        :param rows: number of rows the generator will yield
        :param indent: number of spaces to indent the fields
        :return: string
        """

        block = [self._create_entry(spec) for _ in range(rows)]
        return json.dumps(block, indent=indent)

    def _create_entry(self, spec: list) -> OrderedDict:
        entry = OrderedDict()
        for label, provider_name, *options in spec:
            if isinstance(provider_name, list):
                entry[label] = self._create_entry(provider_name)
            else:
                params = options[0] if options else {}
                provider = getattr(self._factory, provider_name)
                entry[label] = provider(**params) if callable(provider) else ""
        return entry
