

def minimum_maximum(*getallen):
    minimum = getallen[0]
    maximum = getallen[0]
    for getal in getallen[1:]:
        if getal < minimum:
            minimum = getal
        if getal > maximum:
            maximum = getal
    return minimum, maximum


def f(*args, **kwargs):
    print('args', args)
    print('kwargs', kwargs)





if __name__ == '__main__':

    print( minimum_maximum(8, 4) )
    print( minimum_maximum(8, 4, 9, 2, 5, 1, 8) )

    minimum, maximum = minimum_maximum(8, 4, 9, 2, 5, 1, 8)
    print(f'minimum: {minimum}, maximum: {maximum}')

    f(1)
    f(2, 7, 3, factor=10)
    f('a', 'b', 11, prefix='>>>', postfix='<<<')

    import random
    getallen = [random.randint(1, 100) for _ in range(15)]

    print(getallen)

    print( minimum_maximum(*getallen) )

    settings = {
        'color': 'red',
        'size': 12,
        'marker': 'd'
    }

    f(*getallen, color='red', size=12, marker='d')
    f(*getallen, **settings)

