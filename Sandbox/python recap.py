

# Variables

# int
n = 12

print( n )
print( type(n) )

# float
x = 2.5493875894573459873459845379384573459745393457983457

print( x )
print( type(x) )


# string
s = 'abcdefghijklmnopqrstuwvxyz'
s = "ABCDEFGHIJKLMNOPQRSTUWVXYZ"

print( s )
print( type(s) )

# string methods
print( s.lower() )
print( s.upper() )
print( s.capitalize() )
print( s.capitalize().swapcase() )

# arithmetic operators
n1 = 37
n2 = 8

print( n1 + n2 )
print( n1 - n2)
print( n1 * n2 )
print( n1 / n2 )
print( n1 // n2 )   # floored division
print( n1 % n2 )    # modulo - remainder after floored division
print( n1 ** n2 )   # power

# math library
import math
print( dir(math) )

print( math.sqrt(64) )

from math import pi
print( pi )

# random library
import random

print( dir(random) )
print( random.randint(1, 100) )
