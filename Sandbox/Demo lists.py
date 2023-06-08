
getallen = [121, 234, 365, 54, 65]

# x, y ,z

x = getallen[0]
y = getallen[1]
z = getallen[-1]

# of met unpacking

x, y, z, *rest = getallen

print(x, y, z)

print(rest)

#----------------------------------

lijst_van_coordinaten = [
    [65, 234, 365],
    [45, 43, 534],
    [121, 54, 567],
    [23, 23, 67],
    [121, 5, 435],
    [78, 234, 9]
]

for x, y, z in lijst_van_coordinaten:
    print(z)

# -------------------------------------------

# list comprehension

print(getallen)

squares = [getal ** 2 for getal in getallen]

print(squares)

print(':'.join([str(x) for x in squares]))

import random

getallen = [random.randint(1, 100) for i in range(30)]

# or

getallen = []
for i in range(30):
    getallen.append(random.randint(1, 100))



print(getallen)


