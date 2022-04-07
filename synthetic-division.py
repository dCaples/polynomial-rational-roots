def synthetic_division(divide_root, coefficients):
    divide_root = divide_root*-1
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
            out_array.append(out_array[-1]*divide_root + coefficients[k])
            k+=1
    # if the last element is not zero, than the possible root is not a root of the polynomial
    if out_array[-1] != 0:
        return False
    else:
        # remove last element
        out_array.pop()
        return out_array

print(synthetic_division(1, [1, 2, 1]))


