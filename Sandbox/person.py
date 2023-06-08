
class Person:

    __slots__ = ['_name', '_residence']

    def __init__(self, name, residence):
        self._name = name
        self._residence = residence

    def tell(self):
        return f'Ik ben {self._name} en ik woon in {self._residence}.'

    def move(self, new_residence):
        self._residence = new_residence

    def __str__(self):
        return f'Persoon: {self._name} uit {self._residence}'

    def __repr__(self):
        return f'Persoon("{self._name}", "{self._residence}")'


# --------------------------

if __name__ == '__main__':

    deelnemers = []
    deelnemers.append(Person('Peter', 'Lhee'))
    deelnemers.append(Person('Dave', 'Naaldwijk'))
    deelnemers.append(Person('Jori', 'Stroe'))

    for deelnemer in deelnemers:
        print(deelnemer)
