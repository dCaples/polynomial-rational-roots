

import math


def primefactors(n):
    factors = []
    #even number divisible
    while n % 2 == 0:
        factors.append(2)
        n = n / 2
    
    #n became odd
    for i in range(3,int(math.sqrt(n))+1,2):
        while (n % i == 0):
            factors.append(i)
            n = n / i
    
    if n > 2:
        factors.append(n)
    if factors == []:
        factors.append(1)
    return factors

print(primefactors(1))