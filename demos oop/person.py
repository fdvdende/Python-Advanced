
class Person:

    __slots__ = ('_name', '_residence', '_age')

    def __init__(self, name: str, residence: str = 'unknown', age: int = None):
        self._name = name
        self._residence = residence
        self._age = age

    def __repr__(self) -> str:
        return f"Person('{self._name}', '{self._residence}')"

    def __str__(self) -> str:
        return f"A person called {self._name} living at {self._residence}. Age {self._age}."

    def __eq__(self, other) -> bool:
        return self._age == other._age
    def __ne__(self, other) -> bool:
        return self._age != other._age
    def __gt__(self, other) -> bool:
        return self._age > other._age
    def __ge__(self, other) -> bool:
        return self._age >= other._age
    def __lt__(self, other) -> bool:
        return self._age < other._age
    def __le__(self, other) -> bool:
        return self._age <= other._age

    def __add__(self, other) -> int:
        if isinstance(other, Person):
            return self._age + other._age
        else:
            raise TypeError('Cannot add Person to an object of another class.')

    def __hash__(self):
        return hash(self._name)

    def tell(self):
        return('I am {} and I live in {}'.format(self._name, self._residence))

    def move(self, new_residence):
        self._residence = new_residence


class Logger:

    PROMPT = '>>>'

    def log1(self, s):
        print(Logger.PROMPT, s)

    @staticmethod
    def log2(s: str):
        print(Logger.PROMPT, s)

    @classmethod
    def log3(cls, s: str):
        print(cls.PROMPT, s)


class Customer(Person, Logger):

    __slots__ = ('_customernr',)

    def __init__(self, name: str, residence: str = 'unknown', age: int = None, customernr = None):
        super().__init__(name, residence, age)

        self._customernr = customernr

    def __repr__(self) -> str:
        return f"Customer('{self._name}', '{self._residence}')"

    def __str__(self) -> str:
        Logger.log2('Been there')
        return f"A customer called {self._name} living at {self._residence}. Age {self._age}."

    @property
    def customernr(self):
        return '>>> ' + self._customernr.upper() + ' <<<'

    @customernr.setter
    def customernr(self, value):
        self._customernr = f'ABC{value:>08}'


if __name__ == '__main__':

    p1 = Customer('Peter', 'Lhee', 66, 'ABC3243')
    print(p1.tell())

    print(p1.customernr)

    p1.customernr = '007'

    print(p1.customernr)
