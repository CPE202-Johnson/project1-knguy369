# int -> string
#returns a string of the num in the base b
def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    rem = num % b
    if b >= 10  and rem >= 10: #new symbol to add for bases > 10
        syms = "ABCDEFG"
        new_sym = syms[rem % 10]
    else: #new symbol to add for all other cases
        new_sym = str(rem)
    if num // b == 0: #base case, when quotient is 0
        return new_sym
    reduced = convert(num // b, b)
    combined = str(reduced) + new_sym
    return combined




