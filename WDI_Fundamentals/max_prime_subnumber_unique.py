import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def has_unique_digits(n):
    digit_set = set()
    temp = n
    if n == 0: return True
    while temp > 0:
        digit = temp % 10
        if digit in digit_set:
            return False
        digit_set.add(digit)
        temp //= 10
    return True


def find_largest_valid_subnumber(number):
    max_found = 0
    length = int(math.log10(number)) + 1
    mask = 10 ** length

    while mask > 0:
        left_peeled = number % mask
        temp = left_peeled

        while temp > 0:
            if is_prime(temp) and has_unique_digits(temp):
                if temp > max_found:
                    max_found = temp
            temp //= 10

        mask //= 10

    return max_found