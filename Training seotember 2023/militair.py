from enum import Enum


class OPCOs(Enum):
    CZSK = 'CZSK'
    CLSK = 'CLSK'
    CLAS = 'CLAS'
    KMAR = 'KMAR'
    BS = 'BS'


class GENDERs(Enum):
    m = 'm'
    v = 'v'
    x = 'x'


class Militair:
    """A class defining a Dutch militair

    Attributes:
        '_rank',
        '_name',
        '_function',
        '_opco',
        '_gender'"""

    __slots__ = ('_rank', '_name', '_function', '_opco', '_gender')

    def __init__(self, rank: str, name: str, function: str, opco: OPCOs, gender: GENDERs):
        self._rank: str = rank
        self._name: str = name
        self._function: str = function
        self._opco: OPCOs = opco
        self._gender: GENDERs = gender

    def __str__(self):
        return f'{self._rank} {self._name} - {self._function} - {self._opco.value}'

    def salutation(self):
        """define salutation"""
        match self._gender:
            case Militair.GENDERs.m: return 'Mr'
            case Militair.GENDERs.v: return 'Mrs'
            case _: return ''

    # getters

    @property
    def name(self):
        salutation = self.salutation()
        return f'{salutation} {self._name}'

    @property
    def rank(self):
        return self._rank.upper()

    @property
    def function(self):
        return self._function

    @property
    def opco(self):
        return self._opco.value

    # setters

    @rank.setter
    def rank(self, value):
        self._rank = value

    @function.setter
    def function(self, value):
        self._function = value

    @opco.setter
    def opco(self, value):
        self._opco = value


# ---------------------------------

if __name__ == '__main__':

    p1 = Militair('LTZ1', 'van der Rijk', 'HTD', Militair.OPCOs.CZSK, Militair.GENDERs.m)

    print( p1 )

    print( p1.name )

    p1.function = 'OpperHTD'
    print( p1 )

