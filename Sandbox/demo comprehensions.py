import random

getallen = [random.randint(1, 100) for i in range(30)]
print(getallen)

kwadraten = [getal ** 2 for getal in getallen]
print(kwadraten)

kwadraten = [getal ** 2 for getal in getallen if getal >= 20 and getal <= 30]
kwadraten = [getal ** 2 for getal in getallen if 20 <= getal <= 30]
print(kwadraten)

kwadraten = {getal: getal ** 2 for getal in getallen}
print(kwadraten)

kwadraten = (getal ** 2 for getal in getallen)
print(kwadraten)

for x in kwadraten:
    print(x)


zin = 'De kat krapt de krullen van de trap'
woorden = zin.lower().split()
print(woorden)

print(' '.join(woorden))

print(sorted(woorden))

print(sorted(woorden, reverse=True))

print(sorted(woorden, key=len, reverse=True))

def aantal_a(woord):
    return woord.count('a')

print( aantal_a(zin) )

print( sorted(woorden, key=aantal_a, reverse=True) )

print( sorted(woorden, key = lambda woord: woord.count('a'), reverse=True) )
print( sorted(woorden, key = lambda woord: woord.count('e'), reverse=True) )
print( sorted(woorden, key = lambda woord: woord.count('l'), reverse=True) )

print( sorted(woorden, key = lambda woord: woord.count('z'), reverse=True) )

print( list(filter(lambda woord: 'k' in woord, woorden)) )

print( list(map(lambda woord: woord.upper() if 'k' in woord else woord, woorden)) )

