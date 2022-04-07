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
    return factors
 
class Number:
    def __init__(self, value):
        self.value = value
        self.factors = primefactors(abs(value))
        # get the sign of value
        if value < 0:
            self.sign = -1
        else:
            self.sign = 1
    def update_value(self):
        self.value = 1
        for factor in self.factors:
            self.value *= factor
        self.value *= self.sign

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.value = numerator.value/denominator.value
        # reduce the fraction by cancelling common factors
        # for each factor in the numerator go through the denominator and cancel it out
        for factor in self.numerator.factors:
            for denom_factor in self.denominator.factors:
                if factor == denom_factor:
                    # set both to 1
                    self.numerator.factors.remove(factor)
                    self.denominator.factors.remove(denom_factor)
        # if the numerator is empty, add 1 to it
        if len(self.numerator.factors) == 0:
            self.numerator.factors.append(1)
        # if the denominator is empty, add 1 to it
        if len(self.denominator.factors) == 0:
            self.denominator.factors.append(1)
        # find the fraction sign
        self.sign = self.numerator.sign * self.denominator.sign
    def update_value(self):
        # the numerator value is the product of numerator factors
        self.numerator.value = 1
        for factor in self.numerator.factors:
            self.numerator.value *= factor
        # the denominator value is the product of denominator factors
        self.denominator.value = 1
        for factor in self.denominator.factors:
            self.denominator.value *= factor
        # update the value of the fraction
        self.value = self.numerator.value/self.denominator.value * self.sign


def multiply(num1, num2):
    # the numbers can either be fractions or numbers
    # if the numbers are numbers, convert them to fractions
    if type(num1) == Number:
        num1 = Fraction(num1, Number(1))
    if type(num2) == Number:
        num2 = Fraction(num2, Number(1))
    # multiply the fractions
    # start by adding the numerator factor lists together
    numerator_factors = num1.numerator.factors + num2.numerator.factors
    # add the denominator factor lists together
    denominator_factors = num1.denominator.factors + num2.denominator.factors
    # multiply the numerator factors
    numerator_value = 1
    for factor in numerator_factors:
        numerator_value *= factor
    # multiply the denominator factors
    denominator_value = 1
    for factor in denominator_factors:
        denominator_value *= factor
    # create the new fraction
    new_fraction = Fraction(Number(numerator_value), Number(denominator_value))
    # set sign of the fraction
    new_fraction.sign = num1.sign * num2.sign
    # update the value of the fraction
    new_fraction.update_value()
    return new_fraction

fraction_1 = Fraction(Number(-4), Number(8))
fraction_2 = Fraction(Number(-2), Number(3))
multiplied = multiply(fraction_1, fraction_2)
print(multiplied.numerator.factors)
print(multiplied.denominator.factors)
print(multiplied.sign)
