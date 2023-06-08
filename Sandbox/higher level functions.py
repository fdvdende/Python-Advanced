

def log(s):
    print('->', s)


def logger(f):
    def inner1(*args):
        log(args)
        return f(*args)
    return inner1


def memoize(fnc):
    cache = {}
    def inner(*args):
        if args in cache:
            return cache[args]
        cache[args] = fnc(*args)
        return cache[args]
    return inner


@memoize
def add(x, y):
    return x + y


def addone(y):
    def add(x):
        return x + y
    return add


# ---------------------------------

log('I am here')

print(add(1,2))

log('Been there')


f = addone(2)

print(f(10))