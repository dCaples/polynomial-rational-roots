
    # plug possible roots into the polynomial
    roots = []
    # continue to synthetic divide until the polynomial can no longer be divided
    division_possible = True
    while division_possible:
        # try to divide the polynomial by the possible roots
        division_possible = False
        for possible_root in possible_roots:
            # if the polynomial can be divided by the possible root
            if synthetic_division(possible_root[2], polynomial_coefficients):
                # add the possible root to the roots list
                roots.append(possible_root[2])
                # the new polynomial is the remainder of the division
                division_result = synthetic_division(possible_root[2], polynomial_coefficients)
                # the result of division is forwards, but the coefficients are backwards
                # so reverse the coefficients
                division_result.reverse()
                # the new polynomial is the remainder of the division
                polynomial_coefficients = division_result
                division_possible = True
        # if the polynomial can no longer be divided, division_possible is false, and the loop will end