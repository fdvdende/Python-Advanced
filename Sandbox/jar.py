import random

class Jar:

    def __init__(self, aantal_rood = None, aantal_groen = None, aantal_paars = None):
        if aantal_rood is None:
            self._aantal_rood = random.randint(1, 1000)
        if aantal_groen is None:
            self._aantal_groen = random.randint(1, 1000)
        if aantal_paars is None:
            self._aantal_paars = random.randint(1, 1000)

    @property
    def aantal_knikkers(self):
        return self._aantal_rood + self._aantal_groen + self._aantal_paars

    def __repr__(self):
        return f'Jar({self.aantal_knikkers})'

    def __str__(self):
        return f'Jar met {self.aantal_knikkers} knikkers.'

    # def __add__(self, other):
    #     return Jar(self._aantal_knikkers + other._aantal_knikkers)
    #
    # def __gt__(self, other):
    #     return self._aantal_knikkers > other._aantal_knikkers
    # def __ge__(self, other):
    #     return self._aantal_knikkers >= other._aantal_knikkers
    # def __lt__(self, other):
    #     return self._aantal_knikkers < other._aantal_knikkers
    # def __le__(self, other):
    #     return self._aantal_knikkers <= other._aantal_knikkers
    # def __eq__(self, other):
    #     return self._aantal_knikkers == other._aantal_knikkers
    # def __ne__(self, other):
    #     return self._aantal_knikkers != other._aantal_knikkers

    def gok(self, n):
        if n > self.aantal_knikkers:
            return 'lager'
        elif n < self.aantal_knikkers:
            return 'hoger'
        else:
            return 'JA'

# ------------------------------------

jar1 = Jar()
jar2 = Jar()

print(jar1)
print(jar2)

# jar_totaal = jar1 + jar2
#
# print(jar_totaal)
#
# if jar1 > jar2:
#     print('jar1 heeft meer knikkers')
# elif jar1 < jar2:
#     print('jar2 heeft meer knikkers')
# else:
#     print('jar1 en jar2 hebben even veel knikkers')
#
# print(jar1 > jar2)
# print(jar1 >= jar2)
# print(jar1 < jar2)
# print(jar1 <= jar2)
# print(jar1 == jar2)
# print(jar1 != jar2)

# while True:
#     n = int(input('Hoeveel klinkers zitten er in de pot? :'))
#     result = jar1.gok(n)
#     print(result)
#     if result.lower() == 'ja':
#         break

print( jar1.aantal_knikkers )
print( jar2.aantal_knikkers )

