# ask user for first and last coefficients of a polynomial
first = int(input("Enter the first coefficient: "))
last = int(input("Enter the last coefficient: "))

# find the prime factors of the first and second polynomial and put it in a list
first_factors = []
last_factors = []

def prime_factors(n):
    factor_list = []
    i = 1
    while i <= n:
        if n % i == 0:
            factor_list.append(i)
            i += 1
        else:
            i += 1
    return factor_list

first_factors = prime_factors(first)
last_factors = prime_factors(last)

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
        divide_root = divide_root*-1
        elements_number = len(coefficients)
        last_element_index = elements_number - 1
        k = last_element_index
        out_array = []
        while k >= 0:
            if k == last_element_index:
                out_array.append(coefficients[k])
                k-=1
                # go to top of while loop 
                continue
            else:
                out_array.append(out_array[-1]*divide_root + coefficients[k])
                k-=1
        # if the last element is not zero, than the possible root is not a root of the polynomial
        if out_array[-1] != 0:
            return False
        else:
            # remove last element
            out_array.pop()
            return out_array
    # test the synthetic division function
    # print testing synthetic division function
    print(synthetic_division(-3, polynomial_coefficients))

    # synthetic divide until the polynomial can no longer be divided




    # plug possible roots into the polynomial
    roots = []
    for root in possible_roots:
        output = 0
        for i in range(polynomial_degree + 1):
            output += polynomial_coefficients[i]*(root[2]**i)
        if output == 0:
            roots.append(root)

    # print the roots in latex form
    print("the roots are: ")
    # create a list of the latex forms
    roots_latex = []
    for root in roots:
        roots_latex.append("\\frac{" + str(root[0]) + "}{" + str(root[1]) + "}")
    # create a string with all of the roots in latex form
    roots_latex_string = ""
    for root in roots_latex:
        roots_latex_string += root + ", "
    # remove last comma and space if there are roots
    if roots_latex_string != "":
        roots_latex_string = roots_latex_string[:-2]

    # print the string
    print(roots_latex_string)
else:
    print("Thank you for using this program!")