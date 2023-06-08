import random

getallen = [random.randint(1, 100) for _ in range(20)]

print(getallen)

print( sorted(getallen) )
print( sorted(getallen, reverse=True) )

def afstand_tot_getal(getal):
    def f(x):
        nonlocal getal
        return abs(x - getal)
    return f

def afstand_tot_50(getal):
    return abs(getal - 50)

print( '>>>', sorted(getallen, key = afstand_tot_getal(40)) )


from functools import partial

def afstand_tot_getal(x, getal):
    return abs(x - getal)

print( sorted(getallen, key = partial(afstand_tot_getal, getal = 30)) )

print( filter(lambda getal: getal < 20, getallen) )
print( list(filter(lambda getal: getal < 20, getallen)) )
print( [getal for getal in getallen if getal < 20] )


print( map(lambda getal: getal/10, getallen) )
print( list(map(lambda getal: getal/10, getallen)) )
print( [getal/10 for getal in getallen] )

from functools import reduce

print( reduce(lambda getal, result: getal if getal < result else result, getallen) )

print( sum(getallen) )