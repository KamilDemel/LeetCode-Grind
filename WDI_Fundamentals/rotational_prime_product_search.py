import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def has_prime_digit_product(number, base):
    product = 1
    temp = number
    while temp > 0:
        digit = temp % base
        product *= digit
        temp //= base
    return is_prime(product)

def rotate_decimal(number):
    if number < 10:
        return number
    length = int(math.log10(number)) + 1
    mask = 10 ** (length - 1)
    last_digit = number % 10
    remaining = number // 10
    return last_digit * mask + remaining

def find_valid_base_with_rotation(number):
    length = int(math.log10(number)) + 1
    for base in range(2, 17):
        rotated_temp = number
        for _ in range(length):
            if has_prime_digit_product(rotated_temp, base):
                return base
            rotated_temp = rotate_decimal(rotated_temp)
    return None