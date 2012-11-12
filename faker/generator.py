import re
import random

class Generator(object):

    def __init__(self):
        self.providers = []
        self.formatters = {}


    def addProvider(self, provider):

        self.providers.insert(0, provider)

    def getProviders(self):

        return self.providers

    def seed(self, seed=None ):

        random.seed(seed)

    def format(self, formatter):
        return self.getFormatter(formatter)

    def getFormatter(self, formatter):
        if formatter in self.formatters:
            return self.formatters[formatter]
        for provider in self.providers:
            if hasattr(provider, formatter):
                self.formatters[formatter] = getattr(provider, formatter)
                return self.formatters[formatter]

        raise ValueError('Unknown formatter "%s"' % formatter)

    def parse(self, text):
        """
        Replaces tokens ('{{ tokenName }}') with the result from the token method call
        """
        return re.sub( r'\{\{\s?(\w+)\s?\}\}', self.callFormatWithMatches , text )

    def callFormatWithMatches(self, matches):
        return self.format( matches.group(1) )()

    def __getattr__(self, item):
        return self.format( item )