import nanoscipy.util as nsu
import numpy as np
import sympy as sp
import scipy.constants as spc


def basic_operations(operator, fir_int, sec_int=None):
    """
    Perform basic operations on two numeric values.

    Parameters
        operator : str
            The operator representing, which operation is to be performed on the two values. Options: '+', '-', '+-',
            '*', '*-', '/', '/-', '^', '^-', '!'.
        fir_int : float
            The first value.
        sec_int : float, optional
            The second value. The default is None.

    Returns
        Product of the operation.
    """

    # check if any of the variables are of type nan
    if 'n' in (fir_int, sec_int):
        # if true, output nan result
        return np.float64('nan')

    if operator == '+':
        opr_res = fir_int + sec_int
    elif operator in ('-', '+-'):
        opr_res = fir_int - sec_int
    elif operator == '*':
        opr_res = fir_int * sec_int
    elif operator == '*-':
        opr_res = fir_int * - sec_int
    elif operator == '/':
        opr_res = fir_int / sec_int
    elif operator == '/-':
        opr_res = fir_int / - sec_int
    elif operator == '^':
        opr_res = fir_int ** sec_int
    elif operator == '^-':
        opr_res = fir_int ** - sec_int
    elif operator == '!':
        try:
            opr_res = np.math.factorial(nsu.float_to_int(fir_int, 'error'))
        except TypeError:
            opr_res = sp.gamma(fir_int + 1)
    else:
        opr_res = None
    return opr_res


def basic_parser(math_string_float, math_ops, direction='ltr', steps=False):
    """
    Operation parser that will perform operations according to the set operators.

    Parameters
        math_string_float : list
            Contains all the values of the mathematical 'string' as floats, whilst the operators are all strings.
        math_ops : tuple
            Contains all the operators that should be recognized in the particular mathematical 'string'.
        direction : str, optional
            Determines in which direction the while loop iterates. Options are from left to right (ltr), and from right
            to left (rtl). The default is 'ltr'.
        steps : bool, optional
            If True, displays balances from the script, whilst performing the operations. The default is False.

    Returns
        Updated string with the performed operations appended in the correct positions.
    """
    if any(i in math_string_float for i in math_ops):
        pre_index_chain = nsu.indexer(math_string_float)  # define index chain
        opr_id = [i for i, e in pre_index_chain if e in math_ops]  # find the index for the given operations

        # iterate over operators and execute in the set direction with the set initial iteration
        if direction == 'ltr':
            iterative = 0
        elif direction == 'rtl':
            iterative = len(math_string_float) - 1
        else:
            raise ValueError(f'Undefined direction {direction}.')
        temp_operations = math_string_float  # define temporary string
        temp_index_chain = pre_index_chain  # define temporary index
        temp_opr_id = opr_id  # define temporary operation index
        while iterative in (i for i, e in pre_index_chain):
            if iterative in temp_opr_id:  # if the iterator is an operator, perform operation, append and update string
                if math_ops == ('!',):  # if the given operation is a factorial

                    # perform operation and define exclusion
                    opr_res_temp = basic_operations(temp_operations[iterative], temp_operations[iterative - 1])
                    int_excl = [iterative - 1]
                else:
                    opr_res_temp = basic_operations(temp_operations[iterative], temp_operations[iterative - 1],
                                                    temp_operations[iterative + 1])  # perform operation
                    int_excl = [iterative - 1, iterative + 1]  # define exclusions

                # update temporary string according to exclusions and iterative index
                temp_operations = [opr_res_temp if k == iterative else j for k, j in temp_index_chain if k not in
                                   int_excl]
                temp_index_chain = nsu.indexer(temp_operations)  # update temporary index
                temp_opr_id = [i for i, e in temp_index_chain if e in math_ops]  # update temporary operation index
                if steps:
                    print(nsu.list_to_string(temp_operations))
                continue

            # update iterator depending on the direction
            if direction == 'ltr':
                iterative += 1
            if direction == 'rtl':
                iterative -= 1
        opr_string = temp_operations  # define a new string post operations
    else:
        opr_string = math_string_float  # if no operations were done, define post string as input string
    return opr_string


def number_parser(math_string):
    """
    Separates numbers in a list from a string. Supports scientific notation.

    Parameters
        math_string : str
            The mathematical string to perform separation on.

    Returns
        List containing the elements from the string, with the numbers separated.
    """
    pre_float_string = [i for i in math_string]  # decompose input string into elements in a list
    pre_index_chain = nsu.indexer(pre_float_string)  # index the constructed list

    # fix decimals and greater than 1-digit numbers
    # temporary elements to be updated upon valid iterative
    i = 0
    temp_string = pre_float_string
    temp_index_chain = pre_index_chain
    while i < len(temp_string):  # iterate over the length of the 1-piece list
        i0_val = temp_string[i]  # i'th value of the 1-piece list
        ip1, im1, ip2, ip3, ip4 = i + 1, i - 1, i + 2, i + 3, i + 4  # define surrounding i´th values
        im1_val = ip1_val = ip2_val = ip3_val = ip4_val = ''
        try:  # try to find the surrounding values, if no such values, pass
            im1_val = temp_string[im1]
        except IndexError:
            pass
        try:
            ip1_val = temp_string[ip1]
            ip2_val = temp_string[ip2]
            ip3_val = temp_string[ip3]
            ip4_val = temp_string[ip4]
        except IndexError:
            pass

        # if the current value is an int and next value is an int or a dot, concatenate the two 1-pieces and make a new
        #   updated list with the concatenated element
        if isinstance(nsu.string_to_float(i0_val), float) and (isinstance(nsu.string_to_int(ip1_val), int) or
                                                               ip1_val == '.'):
            temp_string = [''.join([i0_val, ip1_val]) if k == i else j for k, j in temp_index_chain if k != ip1]
            temp_index_chain = nsu.indexer(temp_string)
            continue  # break and restart loop with the updated list

        # if the current string value's last element is a dot, and the next element is an int, concatenate and update
        elif [h for h in i0_val][-1] == '.' and isinstance(nsu.string_to_int(ip1_val), int):
            temp_string = [''.join([i0_val, ip1_val]) if k == i else j for k, j in temp_index_chain if k != ip1]
            temp_index_chain = nsu.indexer(temp_string)
            continue  # break and restart loop with the updated list

        # if the current string value has a consecutive e-/+[int], join
        elif i0_val == 'e' and (ip1_val in ('+', '-') or isinstance(nsu.string_to_int(ip1_val), int)):
            if ip1_val in ('+', '-'):
                temp_string = [''.join([im1_val, i0_val, ip1_val, ip2_val]) if k == i else j for k, j in
                               temp_index_chain if k not in (im1, ip1, ip2)]
            elif isinstance(nsu.string_to_int(ip1_val), int):
                temp_string = [''.join([im1_val, i0_val, ip1_val]) if k == i else j for k, j in temp_index_chain if
                               k not in (im1, ip1)]
            temp_index_chain = nsu.indexer(temp_string)
            i -= 1
            continue  # break and restart loop with the updated list

        # if the string contains key values pi, replace those with the value of pi
        elif i0_val == 'p' and ip1_val == 'i':
            temp_string = [str(np.pi) if k == i else j for k, j in temp_index_chain if k != ip1]
            temp_index_chain = nsu.indexer(temp_string)
            continue  # break and restart loop with the updated list

        # replace natural constants
        elif i0_val == '_':
            if (ip1_val, ip2_val, ip3_val, ip4_val) == ('h', 'b', 'a', 'r'):
                temp_string = [str(spc.hbar) if k == i else j for k, j in temp_index_chain if k not in (ip1, ip2, ip3,
                                                                                                        ip4)]
            elif (ip1_val, ip2_val) == ('N', 'A'):
                temp_string = [str(spc.N_A) if k == i else j for k, j in temp_index_chain if k not in (ip1, ip2)]
            elif ip1_val == 'c':
                temp_string = [str(spc.c) if k == i else j for k, j in temp_index_chain if k != ip1]
            elif ip1_val == 'h':
                temp_string = [str(spc.h) if k == i else j for k, j in temp_index_chain if k != ip1]
            elif ip1_val == 'e':
                temp_string = [str(spc.e) if k == i else j for k, j in temp_index_chain if k != ip1]
            elif ip1_val == 'R':
                temp_string = [str(spc.R) if k == i else j for k, j in temp_index_chain if k != ip1]
            elif ip1_val == 'k':
                temp_string = [str(spc.k) if k == i else j for k, j in temp_index_chain if k != ip1]
            else:
                raise ValueError('Constant is not defined in parser.')
            temp_index_chain = nsu.indexer(temp_string)

        # if two negative signs are consecutive, change to a positive sign
        elif i0_val == '-' and ip1_val == '-':
            temp_string = ['+' if k == i else j for k, j in temp_index_chain if k != ip1]
            temp_index_chain = nsu.indexer(temp_string)
            continue
        i += 1  # update iterator
    return temp_string


def ordered_parser(math_string, steps=False):
    """
    Performs operations on the given string in an ordered way. Firstly, powers are executed, secondly, products and
    divisions and at last additions and subtractions.

    Parameters
        math_string : str
            Contains the mathematical expression in a string.
        steps : bool, optional
            If True, displays balances from the script, whilst performing the operations. The default is False.

    Returns
        A float representing the result of the executed operations.
    """
    parsed_numbers = number_parser(math_string)  # fix numbers in passed string
    # if the first value of the fixed list is a '-', append to the next value, preventing interpretation as an operator
    if parsed_numbers[0] in ('-', '+'):
        post_float_string = [''.join([parsed_numbers[0], parsed_numbers[1]]) if i == 0 else j for i, j in
                             nsu.indexer(parsed_numbers) if i != 1]
    else:
        post_float_string = parsed_numbers
    post_index_chain = nsu.indexer(post_float_string)  # define index for the fixed string

    # fix negative numbers by creating a negative operator. Note that this prevents powers from interpreting all values
    #   with a negative operator in front as a negative number; hence allows for -2^2=-4 and (-2)^2=4
    # empty lists for appending
    elem_index = []
    elem_excl = []
    for i, j in post_index_chain:
        i_next = i + 1
        j_next = None
        try:  # try to find the next values, if no such value, pass
            j_next = post_float_string[i_next]
        except IndexError:
            pass

        # if two elements are x and y, make a collective xy element, in place of x, and define exclusion index of y
        if (j, j_next) == ('*', '-'):
            elem = '*-'
            elem_excl.append(i_next)
        elif (j, j_next) == ('/', '-'):
            elem = '/-'
            elem_excl.append(i_next)
        elif (j, j_next) == ('^', '-'):
            elem = '^-'
            elem_excl.append(i_next)
        elif (j, j_next) == ('+', '-') or (j, j_next) == ('-', '+'):
            elem = '+-'
            elem_excl.append(i_next)
        else:  # for all other elements, define current iterative as value
            elem = j
        elem_index.append([i, elem])

    # define new list of strings: replace elements that should be collective elements, and remove excess defined by
    #   elem_excl
    float_string_str = [i[1] if i != j else j[1] for i, j in zip(elem_index, post_index_chain) if j[0] not in elem_excl]
    float_string = [nsu.string_to_float(i) for i in float_string_str]  # convert string to float if possible

    # check for 1. default operation order
    o1_opr_string = basic_parser(float_string, ('^', '^-'), 'rtl', steps)

    # check for 2. default operation order
    o2_opr_string = basic_parser(o1_opr_string, ('!',), 'ltr', steps)

    # check for 3. default operation order
    o3_opr_string = basic_parser(o2_opr_string, ('*', '/', '*-', '/-'), 'ltr', steps)

    # check for 4. default operation order
    o4_opr_string = basic_parser(o3_opr_string, ('+', '-', '+-'), 'ltr', steps)

    return o4_opr_string[0]


def product_parser(math_string):
    """
    Parser that detects implicit multiplication and adds appropriate operators in those positions.

    Parameters
        math_string : string
            The mathematical string to search for implicit multiplication.

    Returns
        Updated list with the implicit multiplication as explicit.
    """
    temp_decom_string = [e for e in math_string]  # temp string to be updated
    i = 0  # initial iteration
    while i < len(temp_decom_string):
        i0_val = temp_decom_string[i]  # define current iteration value
        ip1, ip2, ip3 = i + 1, i + 2, i + 3  # define consecutive iterations
        ip1_val = ip2_val = ip3_val = None  # provide standard values for those iterations
        try:  # try to find values for those iterations
            ip1_val = temp_decom_string[ip1]
            ip2_val = temp_decom_string[ip2]
            ip3_val = temp_decom_string[ip3]
        except IndexError:  # if index is surpassed, pass clause at position
            pass

        # determine in which positions to add a '*' and add it
        if (i0_val, ip1_val) == (')', '(') or (isinstance(nsu.string_to_float(i0_val), float) and ip1_val in
                                               (*[i for i in nsu.alphabetSequence if i != 'e'],
                                                *nsu.alphabetSequenceCap, '(')) or \
                (i0_val in (*[i for i in nsu.alphabetSequence if i != 'e'], *nsu.alphabetSequenceCap, ')') and
                 isinstance(nsu.string_to_float(ip1_val), float)) or \
                (isinstance(nsu.string_to_float(i0_val), float) and (ip1_val, ip2_val, ip3_val) == ('e', 'x', 'p')) or \
                (i0_val == ')' and ip1_val in (*nsu.alphabetSequence, *nsu.alphabetSequenceCap)) or \
                ((i0_val, ip1_val) == (')', '_')) or \
                (isinstance(nsu.string_to_float(i0_val), float) and ip1_val == '_') or \
                (i0_val in (*nsu.alphabetSequence, *nsu.alphabetSequenceCap) and ip1_val == '_'):
            temp_decom_string = temp_decom_string[: ip1] + ['*'] + temp_decom_string[ip1:]
        elif (i0_val, ip1_val, ip2_val) == ('p', 'i', '('):
            temp_decom_string = temp_decom_string[: ip2] + ['*'] + temp_decom_string[ip2:]
        i += 1  # update iterator
    return temp_decom_string


def parser(math_string, steps=False, cprint=True):
    """
    Takes care of the additional rules and conventions of mathematical operations. Handles parentheses along with
    operators that require parentheses, such as trigonometric functions (sin, cos, tan, ...) and log, exp, etc.

    Parameters
        math_string : str
            The mathematical string to parse through the interpreter.
        steps : bool, optional
            If True, displays balances from the script, whilst performing the operations. The default is False.
        cprint : bool, optional
            If True, prints the calculation and result. The default is True.

    Returns
        The result from the performed operations on the given mathematical string as a float.
    """
    # define temporary lists/values to be updated from while loop
    temp_decom_string = product_parser(math_string)
    temp_index = nsu.indexer(temp_decom_string)
    temp_bracket_idx = [[j] + [e] for j, e in temp_index if e in ('(', ')')]  # find and index open/close brackets
    if steps:
        print(math_string)
    i = 0  # set starting iteration
    while temp_bracket_idx:
        # if two consecutive brackets are a pair, execute operations through ordered_parser(), append the result to the
        #   given string, update it and reiterate. This ensures that the parentheses are read in the correct order

        try:  # check for missing closing parenthesis
            closing_bracket = temp_bracket_idx[i + 1][1]
        except IndexError:
            raise ValueError('Missing closing bracket somewhere.')

        if temp_bracket_idx[i][1] == '(' and closing_bracket == ')':
            i0, i1 = temp_bracket_idx[i][0], temp_bracket_idx[i + 1][0]  # define current i'th values
            im1, im2, im3, im4, im5, im6 = i0 - 1, i0 - 2, i0 - 3, i0 - 4, i0 - 5, i0 - 6  # define consecutive -i's
            ip1 = i1 + 1  # define consecutive +i's
            bracket_excl = list(range(i0 + 1, ip1))  # define the bracket clause as an exclusion
            new_string = nsu.list_to_string(temp_decom_string[i0 + 1: i1])  # string consisting only of the clause
            pre_temp_result = ordered_parser(new_string, steps)  # execute operations on the clause

            # define temporary lists/values
            id_excl = []
            temp_result = pre_temp_result
            im6_val = im5_val = im4_val = im3_val = im2_val = im1_val = ip1_val = None
            try:  # try to define values for the surrounding iterations, otherwise pass at position
                im1_val = temp_decom_string[im1]
                im2_val = temp_decom_string[im2]
                im3_val = temp_decom_string[im3]
                im4_val = temp_decom_string[im4]
                im5_val = temp_decom_string[im5]
                im6_val = temp_decom_string[im6]
            except IndexError:
                pass
            try:
                ip1_val = temp_decom_string[ip1]
            except IndexError:
                pass

            # if preceding iterations or upcoming operations leads to an identifier, perform special operation on the
            #   clause, respecting order. From here, define temporary result to append, along with index for exclusions
            if (im6_val, im5_val, im4_val, im3_val, im2_val, im1_val) == ('a', 'r', 'c', 's', 'i', 'n') or \
                    (im6_val, im5_val, im4_val, im3_val, im2_val, im1_val) == ('s', 'i', 'n', '^', '-', '1'):
                temp_result = np.arcsin(pre_temp_result)
                id_excl = list(range(im6, i0))
            elif (im6_val, im5_val, im4_val, im3_val, im2_val, im1_val) == ('a', 'r', 'c', 'c', 'o', 's') or \
                    (im6_val, im5_val, im4_val, im3_val, im2_val, im1_val) == ('c', 'o', 's', '^', '-', '1'):
                temp_result = np.arccos(pre_temp_result)
                id_excl = list(range(im6, i0))
            elif (im6_val, im5_val, im4_val, im3_val, im2_val, im1_val) == ('a', 'r', 'c', 't', 'a', 'n') or \
                    (im6_val, im5_val, im4_val, im3_val, im2_val, im1_val) == ('t', 'a', 'n', '^', '-', '1'):
                temp_result = np.tan(pre_temp_result)
                id_excl = list(range(im6, i0))
            elif (im3_val, im2_val, im1_val) == ('e', 'x', 'p'):
                temp_result = np.exp(pre_temp_result)
                id_excl = list(range(im3, i0))
            elif (im3_val, im2_val, im1_val) == ('l', 'o', 'g'):
                if pre_temp_result == 0:
                    raise ValueError('Parser does not support infinity values, log10(0) = -inf.')
                else:
                    temp_result = np.log10(pre_temp_result)
                id_excl = list(range(im3, i0))
            elif (im3_val, im2_val, im1_val) == ('s', 'i', 'n'):
                # fix sin(n*pi) numerical variation for n in NN
                if pre_temp_result == 0:
                    temp_result = 0
                else:
                    arbitrary_x = sp.symbols('arbitraryX')
                    equation_sin_pi_solution = sp.solve(pre_temp_result / arbitrary_x - np.pi)
                    if isinstance(nsu.float_to_int(equation_sin_pi_solution[0]), int):
                        temp_result = 0
                    else:
                        temp_result = np.sin(pre_temp_result)
                id_excl = list(range(im3, i0))
            elif (im3_val, im2_val, im1_val) == ('c', 'o', 's'):
                temp_result = np.cos(pre_temp_result)
                id_excl = list(range(im3, i0))
            elif (im3_val, im2_val, im1_val) == ('t', 'a', 'n'):
                temp_result = np.tan(pre_temp_result)
                id_excl = list(range(im3, i0))
            elif (im3_val, im2_val, im1_val) == ('d', 'e', 'g'):
                temp_result = 360 / (2 * sp.pi) * pre_temp_result
                id_excl = list(range(im3, i0))
            elif (im3_val, im2_val, im1_val) == ('r', 'a', 'd'):
                temp_result = (2 * sp.pi) / 360 * pre_temp_result
                id_excl = list(range(im3, i0))
            elif (im2_val, im1_val) == ('l', 'n'):
                if pre_temp_result == 0:
                    raise ValueError('Parser does not support infinity values, ln(0) = -inf.')
                else:
                    temp_result = np.log(pre_temp_result)
                id_excl = list(range(im2, i0))

            temp_excel = bracket_excl + id_excl  # define all needed exclusions in a list

            # update the temporary string, index, and bracket index and reiterate
            temp_decom_string = [temp_result if k == i0 else j for k, j in temp_index if k not in temp_excel]
            if steps:
                print(nsu.list_to_string(temp_decom_string))
            temp_index = nsu.indexer(temp_decom_string)
            temp_bracket_idx = [[j] + [e] for j, e in temp_index if e in ('(', ')')]
            i -= 1  # reset iteration
            continue
        i += 1
    else:  # if no brackets are present in iterated string, perform operations as usual per ordered_parser()
        new_string = nsu.list_to_string(temp_decom_string)
        parsed_string = ordered_parser(new_string, steps)
        int_fixed_string = nsu.float_to_int(parsed_string)

    # auto-print if prompted
    if cprint:
        pretty_string = nsu.replace(('pi', '_hbar', '_NA', '_c', '_h', '*', '_R', '_k', '_e'),
                                    ('π', 'ħ', 'Nᴀ', 'c', 'h', '⋅', 'R', 'k', 'e'), math_string)
        if isinstance(nsu.float_to_int(int_fixed_string / np.pi), int) and int_fixed_string != 0:
            pi_fixed_string = str(nsu.float_to_int(int_fixed_string / np.pi)) + 'π'
        else:
            pi_fixed_string = int_fixed_string
        print(f'Result: {pretty_string} = {pi_fixed_string}')
    return int_fixed_string
