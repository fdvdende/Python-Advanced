
# pythagoras number: e.g. 3, 4, 5 because 3**2 + 4**2 == 5**2

def pythagoras_numbers(maximum = 100):
    numbers = []
    for a in range(1, maximum + 1):
        for b in range(1, maximum + 1):
            ab = a ** 2 + b ** 2
            c = int(ab ** 0.5)
            if ab == c ** 2:
                numbers.append((a, b, c))
    return numbers


def pythagoras_numbers(maximum = 100):
    for a in range(1, maximum + 1):
        for b in range(1, maximum + 1):
            ab = a ** 2 + b ** 2
            c = int(ab ** 0.5)
            if ab == c ** 2:
                yield (a, b, c)






# for pythagoras_number in pythagoras_numbers(10000):
#     print(*pythagoras_number, sep = ' - ')




numbers = (number ** 3 for number in range(1000000))
for n in numbers:
    print(n)