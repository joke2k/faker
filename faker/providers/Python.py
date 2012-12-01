from . import BaseProvider
from decimal import Decimal
from .Lorem import Provider as Lorem
import sys

class Provider(BaseProvider):

    @classmethod
    def pybool(cls): return cls.randomInt(0,1) == 1

    @classmethod
    def pystr(cls, maxChars=20): return Lorem.text(maxChars)

    @classmethod
    def pyfloat(cls, leftDigits=None, rightDigits=None, positive=False):
        leftDigits = leftDigits or cls.randomInt(1,sys.float_info.dig)
        rightDigits = rightDigits or cls.randomInt(0, sys.float_info.dig-leftDigits)
        sign = 1 if positive or cls.randomInt(0,1) else -1

        return float( "{}.{}".format(
            sign * cls.randomNumber(leftDigits), cls.randomNumber(rightDigits)
        ) )


    @classmethod
    def pyint(cls): return cls.randomInt()

    @classmethod
    def pyunicode(cls, maxChars=20): return unicode(Lorem.text(maxChars))

    @classmethod
    def pydecimal(cls, leftDigits=None, rightDigits=None, positive=False):
        return Decimal(str(cls.pyfloat(leftDigits, rightDigits, positive)))

    def pytuple(self, nbElements=10, variableNbElements=True, *valueTypes):
        return tuple(self.pyset(nbElements, variableNbElements, *valueTypes))

    def pyset(self, nbElements=10, variableNbElements=True, *valueTypes):
        return set(self._pyiterable(nbElements, variableNbElements, *valueTypes))

    def pylist(self, nbElements=10, variableNbElements=True, *valueTypes):
        return list(self._pyiterable(nbElements, variableNbElements, *valueTypes))

    def pyiterable(self, nbElements=10, variableNbElements=True, *valueTypes):
        return self.randomElement([self.pylist,self.pytuple,self.pyset])(nbElements, variableNbElements, *valueTypes)

    def _randomType(self, typesList):
        valueType = self.randomElement( typesList )

        methodName = "py%s" % valueType
        if hasattr(self, methodName):
            valueType = methodName

        return self.generator.format(valueType)

    def _pyiterable(self, nbElements=10, variableNbElements=True, *valueTypes):

        valueTypes = [t if isinstance(t,basestring) else getattr(t,'__name__',type(t).__name__).lower()
                      for t in valueTypes
                      # avoid recursion
                      if t not in ['iterable','list','tuple','dict','set']]
        if not valueTypes:
            valueTypes = ['str','str','str','str','float','int','int','decimal','dateTime','uri','email']

        if variableNbElements:
            nbElements = self.randomizeNbElements( nbElements )

        for f in range( nbElements ):

            yield self._randomType( valueTypes )


    def pydict(self, nbElements=10, variableNbElements=True, *valueTypes):
        """
         Use this function to generate data, returns a touple containing
         a list, a dictionary and a nested dictionary.
         """
        if variableNbElements:
            nbElements = self.randomizeNbElements( nbElements )

        return dict(zip(
            Lorem.words(nbElements),
            self._pyiterable(nbElements,False, *valueTypes)
        ))


    def pystruct(self, count=10, *valueTypes ):

        valueTypes = [t if isinstance(t,basestring) else getattr(t,'__name__',type(t).__name__).lower()
                      for t in valueTypes
                      # avoid recursion
                      if t != 'struct']
        if not valueTypes:
            valueTypes = ['str','str','str','str','float','int','int','decimal','dateTime','uri','email']

        l = []; d = {}; nd = {}
        for i in range(count):
            d[Lorem.word()] = self._randomType( valueTypes )
            l.append(self._randomType( valueTypes ))
            nd[Lorem.word()] = {
                i: self._randomType( valueTypes ),
                i+1: [self._randomType( valueTypes ),self._randomType( valueTypes ), self._randomType( valueTypes )],
                i+2: {
                    i: self._randomType( valueTypes ),
                    i+1:self._randomType( valueTypes ),
                    i+2: [
                        self._randomType( valueTypes ),
                        self._randomType( valueTypes )
                    ]
                }
            }
        return l, d, nd
