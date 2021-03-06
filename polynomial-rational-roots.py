# CAS code
import math

def primefactors(n):
    factors = []
    # if n is zero, return [0]
    if n == 0:
        return [0]
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
        # takes in 2 number objects
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
        # if the numerator and denominator are equal, then the fraction is 1/1
        if self.numerator.factors == self.denominator.factors:
            self.numerator.factors = [1]
            self.denominator.factors = [1]
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

def reciprocal(num):
    # the numbers can either be fractions or numbers
    # if the numbers are numbers, convert them to fractions
    if type(num) == Number:
        num = Fraction(num, Number(1))
    # switch the numerator and denominator
    new_fraction = Fraction(num.denominator, num.numerator)
    # set sign of the fraction
    new_fraction.sign = num.sign
    # update the value of the fraction
    new_fraction.update_value()
    return new_fraction

def add(num1, num2):
    # this only accepts fractions
    # if the numbers are numbers, convert them to fractions
    if type(num1) == Number:
        num1 = Fraction(num1, Number(1))
    if type(num2) == Number:
        num2 = Fraction(num2, Number(1))


    numerator_1 = num1.numerator.value * num1.sign
    numerator_2 = num2.numerator.value * num2.sign

    denominator_1 = num1.denominator.value
    denominator_2 = num2.denominator.value
    common_denominator = denominator_1 * denominator_2

    numerator_1 = numerator_1 * denominator_2
    numerator_2 = numerator_2 * denominator_1

    total_numerator = numerator_1 + numerator_2
    # Fraction method only accepts Number objects
    return Fraction(Number(total_numerator), Number(common_denominator))

def subtract(num1, num2):
    num2.sign = -num2.sign
    return add(num1, num2)
# end CAS code



# ask user for first and last coefficients of a polynomial
first = int(input("Enter the first coefficient: "))
last = int(input("Enter the last coefficient: "))

# find the prime factors of the first and second polynomial and put it in a list
first_factors = []
last_factors = []

def factors(n):
    factor_list = []
    i = 1
    while i <= n:
        if n % i == 0:
            factor_list.append(i)
            i += 1
        else:
            i += 1
    return factor_list

first_factors = factors(first)
last_factors = factors(last)

# generate fractions from factors list
# last factors will be the numerator
# first factors will be the denominator
fractions = []
for numerator in last_factors:
    for denominator in first_factors:
        fractions.append([numerator, denominator])

# reduce any fractions that can be reduced
for fraction in fractions:
    numerator = fraction[0]
    denominator = fraction[1]
    if numerator==denominator:
        numerator = 1
        denominator = 1
        fraction[0] = numerator
        fraction[1] = denominator
        
 # if there is a duplicate fraction, remove it
# while loop to remove duplicate list elements
first_index = 0
second_index = 0
while first_index < len(fractions):
    while second_index < len(fractions):
        # one fraction is the same as another
        # make sure it's not the same fraction as itself
        if fractions[first_index] == fractions[second_index] and first_index != second_index:
            del fractions[second_index]
        else:
            second_index += 1
    first_index += 1

# the fractions could also be negative, so duplicate the list, and make the numerators negative
# we have do deepcopy it so memory isn't shared
def deepcopy(obj):
    if isinstance(obj, dict):
        return {deepcopy(key): deepcopy(value) for key, value in obj.items()}
    if hasattr(obj, '__iter__'):
        return type(obj)(deepcopy(item) for item in obj)
    return obj

negative_fractions = deepcopy(fractions)


fraction_index = 0
print(len(negative_fractions))
while fraction_index < len(negative_fractions):
    negative_fractions[fraction_index][0] = -1*negative_fractions[fraction_index][0]
    fraction_index += 1

# combine the two lists
fractions.extend(negative_fractions)



# print all of the fractions in fraction form
print(fractions)
# create list of fractions in latex \frac{}{} form
fraction_latex = []
for fraction in fractions:
    fraction_latex.append("\\frac{" + str(fraction[0]) + "}{" + str(fraction[1]) + "}")
# create a string with all of the fractions in latex form
fraction_latex_string = ""
for fraction in fraction_latex:
    fraction_latex_string += fraction + ", "
# print the string
print(fraction_latex_string)

# ask user if they would like to check the roots
check_roots = input("Would you like to check the roots? (y/n): ")
# change the check_roots variable to boolean
if check_roots == "y":
    check_roots = True
else:
    check_roots = False

###############################################################################################
#                                   check the roots                                           #
###############################################################################################
# create exact fractions from the list of fractions using fraction and number classes
exact_fractions = []
for fraction in fractions:
    exact_fractions.append(Fraction(Number(fraction[0]), Number(fraction[1])))
print(exact_fractions)


# if check roots is true then ask for the polynomial
if check_roots:
    polynomial_degree = int(input("Enter the degree of the polynomial: "))
    # create a list of the coefficients
    polynomial_coefficients = []
    for i in range(polynomial_degree + 1):
        polynomial_coefficients.append(int(input("Enter the coefficient of x^" + str(i) + ": ")))
    # convert possible root fractions to decimals by dividing
    possible_roots = []
    fraction_index = 0
    while fraction_index < len(fractions):
        # the format of possible roots is [numerator, denominator, decimal]
        # possible_roots.append(fractions[fraction_index][0]/fractions[fraction_index][1])
        possible_roots.append([fractions[fraction_index][0], fractions[fraction_index][1], fractions[fraction_index][0]/fractions[fraction_index][1]])
        fraction_index += 1
    # synthetic division function
    # takes in a list of coefficients and dividing root and outputs false if the polynomial is not a root, and outputs new divided coefficients if it is a root

    def synthetic_division(divide_root, coefficients):
        # coeeficients are fraction objects
        # divide_root is a Fraction object
        divide_root.sign = divide_root.sign * -1
        elements_number = len(coefficients)
        last_element_index = elements_number - 1
        k = 0
        out_array = []
        while k <= last_element_index:
            if k == 0:
                out_array.append(coefficients[k])
                k+=1
                # go to top of while loop 
                continue
            else:
                # out_array.append(out_array[-1]*divide_root + coefficients[k])
                # out_array.append(add(multiply(out_array[-1], divide_root) , coefficients[k]))
                out_array.append(add(multiply(out_array[-1], divide_root) , coefficients[k]))

                k+=1
        if out_array[-1].numerator.value != 0:
            return False
        else:
            out_array.pop()
            return out_array

    out_array = synthetic_division(Fraction(Number(1), Number(1)), [Fraction(Number(1), Number(1)), Fraction(Number(2), Number(1)), Fraction(Number(1), Number(1))])
    for element in out_array:
        # print result of synthetic division
        print(element.numerator.value, element.denominator.value)


else:
    print("Thank you for using this program!")