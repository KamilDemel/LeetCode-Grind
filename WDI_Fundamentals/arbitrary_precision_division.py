def long_division(numerator, denominator, precision=100):
    integer_part = numerator // denominator
    print(integer_part, end=".")

    remainder = numerator % denominator
    for _ in range(precision):
        multiplied_remainder = remainder * 10
        digit = multiplied_remainder // denominator
        print(digit, end="")
        remainder = multiplied_remainder % denominator
    print()