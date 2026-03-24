def calculate_integer_sqrt(n):
    """
    Computes the integer square root of n using the property that 
    the sum of the first k odd numbers is k squared.
    """
    if n < 0:
        raise ValueError("Cannot compute square root of a negative number")

    remainder = n
    root = 0
    current_odd = 1

    while remainder >= current_odd:
        remainder -= current_odd
        root += 1
        current_odd += 2

    return root