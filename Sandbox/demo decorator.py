import logging
import time
import functools


def deco(f):
    def wrapper():
        print('entering function')
        f()
        print('leaving function')
    return wrapper


# example template
def my_decorator(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        # do something
        return_value = f(*args, **kwargs)
        # do something
        return return_value
    return wrapper


def deco(f):
    def wrapper():
        print('entering function')
        f()
        print('leaving function')
    return wrapper


logging.basicConfig(
    filename = None,    # or to a file 'example.log',
    level = logging.DEBUG,   # DEBUG, INFO, WARNING, ERROR, CRITICAL
    format = '%(asctime)s %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S')


def log(f):
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        logging.debug(f"Calling {f.__name__}({signature})")
        t0 = time.perf_counter_ns()
        return_value = f(*args, **kwargs)
        t1 = time.perf_counter_ns()
        logging.debug(f'Executed function {f.__name__} duration in ns {t1 - t0}')
        return return_value
    return wrapper


def cache(f):
    memoire = {}
    def wrapper(*args):
        nonlocal memoire
        if args in memoire.keys():
            return_value = memoire[args]
        else:
            return_value = f(*args)
            memoire[args] = return_value
        return return_value
    return wrapper


def logger(f):
    def wrapper(*args, **kwargs):
        logging.info(f'entering function [{f.__name__}] - args: {args} - kwargs: {kwargs}')
        return_value = f(*args, **kwargs)
        logging.info(f'leaving function [{f.__name__}] - return value: {return_value}')
        return return_value
    return wrapper


def twice(f):
    def wrapper():
        f()
        f()
    return wrapper


@log
def f(message):
    print(message.upper())


@logger
def demo_function(*args, **kwargs):
    print('positional arguments', args)
    print('keyword arguments', kwargs)



@cache
def telop(n):
    total = 0
    for i in range(n):
        total += i
    return total



# demo_function(1,2,3,4,5, flag=True, aantal=10)

# f(message = 'Hi there!!')

t0 = time.time_ns()
print(telop(1000000))
t1 = time.time_ns()
print(telop(1000000))
t2 = time.time_ns()

print('eerste keer', t1 - t0)
print('tweede keer', t2 - t1)

# t0 = time.time_ns()
# print(telop(98789))
# t1 = time.time_ns()
# print(telop(98789))
# t2 = time.time_ns()
#
# print('eerste keer', t1 - t0)
# print('tweede keer', t2 - t1)
#
#
#
# import functools
#
#
# @functools.lru_cache()
# def fibonacci(num):
#     print(f"Calculating fibonacci({num})")
#     if num < 2:
#         return num
#     return fibonacci(num - 1) + fibonacci(num - 2)
#
#
# t0 = time.time_ns()
# print(fibonacci(20))  # 1 1 2 3 5 8 13 21 34 55
# t1 = time.time_ns()
# print('duur', t1 - t0)
