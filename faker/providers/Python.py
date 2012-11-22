from . import BaseProvider
from decimal import Decimal
from .Lorem import Provider as Lorem

class Provider(BaseProvider):

    @classmethod
    def pystr(cls, maxChars=20): return Lorem.text(maxChars)

    @classmethod
    def pyfloat(cls): return float(cls.numerify(cls.randomElement(['#####.##','##.###','#.##','#.####'])))

    @classmethod
    def pyint(cls): return cls.randomInt()

    @classmethod
    def pyunicode(cls, maxChars=20): return unicode(Lorem.text(maxChars))

    @classmethod
    def pydecimal(cls): return Decimal(str(cls.pyfloat()))

    def pytuple(self, nbElements=10, variableNbElements=True, *valueTypes):
        return tuple(self.pyset(nbElements, variableNbElements, *valueTypes))

    def pyset(self, nbElements=10, variableNbElements=True, *valueTypes):
        return set(self._pyiterable(nbElements, variableNbElements, *valueTypes))

    def pylist(self, nbElements=10, variableNbElements=True, *valueTypes):
        return list(self._pyiterable(nbElements, variableNbElements, *valueTypes))

    def pyiterable(self, nbElements=10, variableNbElements=True, *valueTypes):
        return self.randomElement([self.pylist,self.pytuple,self.pyset])(nbElements, variableNbElements, *valueTypes)

    def _pyiterable(self, nbElements=10, variableNbElements=True, *valueTypes):

        valueTypes = [t if isinstance(t,basestring) else getattr(t,'__name__',type(t).__name__).lower()
                      for t in valueTypes
                      # avoid recursion
                      if t not in ['iterable','list','tuple','dict','set']]
        if not valueTypes:
            valueTypes = ['str','str','str','str','float','int','int','decimal','dateTime','uri','email']
#        valueTypes = [t for t in valueTypes if t not in ['iterable','list','tuple','dict','set']]
#        if nbElements <= 0:
#            return []

        if variableNbElements:
            nbElements = Lorem.randomizeNbElements( nbElements )

        for f in range( nbElements ):
            valueType = self.randomElement( valueTypes )
            methodName = "py%s" % valueType
            if hasattr(self, methodName):
                yield getattr(self, methodName)()
            else:
                yield getattr(self.generator, valueType)()

    def pydict(self, nbElements=10, variableNbElements=True, *valueTypes):
        """
         Use this function to generate data, returns a touple containing
         a list, a dictionary and a nested dictionary.
         """
        if variableNbElements:
            nbElements = Lorem.randomizeNbElements( nbElements )

        return dict(zip(
            Lorem.words(nbElements),
            self._pyiterable(nbElements,False, *valueTypes)
        ))


    def pystruct(self, count=10):
        def ipsum(n=1):
            return Lorem.word() if n==1 else Lorem.sentences(n)
        l = []; d = {}; nd = {}
        for i in range(count):
            d[ipsum()] = ipsum(10)
            l.append(ipsum(3))
            nd[ipsum()] = {i: ipsum(), i+1: [ipsum(2), ipsum(4), ipsum(3)], i+2: {i: ipsum(3), i+1: ipsum(4), i+2: [ipsum(2), ipsum(3)]}}

        return l, d, nd