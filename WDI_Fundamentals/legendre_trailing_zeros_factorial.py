def count_trailing_zeros_in_factorial(n):
    count = 0
    power_of_five = 5
    while power_of_five <= n:
        count += n // power_of_five
        power_of_five *= 5
    return count