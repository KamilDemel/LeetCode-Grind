def get_first_three_significant_digits(x):
    if x == 0:
        raise ValueError("Cannot divide by zero")

    numerator = 1

    while numerator < x:
        numerator *= 10

    numerator *= 100

    result = numerator // x
    return result