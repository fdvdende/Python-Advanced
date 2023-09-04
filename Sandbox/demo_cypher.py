from string import ascii_lowercase, digits, punctuation
from time import perf_counter_ns
from functools import lru_cache

alphabet = ascii_lowercase + digits + punctuation

def duration(f):
    def wrapper(*args, **kwargs):
        t0 = perf_counter_ns()
        return_value = f(*args, **kwargs)
        t1 = perf_counter_ns()
        print(f'Duration {f.__name__}: {(t1 - t0)/1000:8.3f} ms')
        return return_value
    return wrapper

def debug(f):
    def wrapper(*args, **kwargs):
        print(f'Calling {f.__name__}({args}, {kwargs}) ==> ', end = '')
        return_value = f(*args, **kwargs)
        print(f'Returns {return_value}')
        return return_value
    return wrapper




@duration
def caesar_encrypt(original, shift = 3):
    substitution = alphabet[shift:] + alphabet[:shift]
    d = dict(zip(alphabet, substitution.upper()))
    encrypted = ''.join(d.get(c, c) for c in original.lower())
    return encrypted

@duration
def caesar_decrypt(encrypted, shift = 3):
    substitution = alphabet[shift:] + alphabet[:shift]
    d = dict(zip(substitution.upper(), alphabet))
    original = ''.join(d.get(c, c) for c in encrypted.upper())
    return original

@duration
# @debug
@lru_cache
def minimum_maximum(*args, **kwargs):
    lowest = args[0]
    highest = args[0]
    for number in args[1:]:
        if number < lowest:
            lowest = number
        if number > highest:
            highest = number
    return lowest, highest


numbers = [34,56,67,23,56,67,45,78,90] * 100

print( minimum_maximum(*numbers) )

print( minimum_maximum(*numbers) )




# original = 'aanvallen xyz 13:00'
#
# encrypted = caesar_encrypt(original, shift = 13)
# decrypted = caesar_decrypt(encrypted, shift = 13)
#
# print( original )
# print( encrypted )
# print( decrypted )