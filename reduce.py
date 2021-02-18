#from __future__ import print_function
from fractions import Fraction
import operator

def product(fracs):
    # complete this line with a reduce statement
    t = reduce(operator.mul, fracs)
    return t.numerator, t.denominator

fracs = []
for _ in range(int(input())):
    fracs.append(Fraction(*map(int, input().split())))
result = product(fracs)
print(*result)
