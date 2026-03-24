import math


def is_perfect(number):
    if number < 2:
        return False
    divisor_sum = 1

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            divisor_sum += i
            j = number // i
            if i != j:
                divisor_sum += j

    if divisor_sum == number:
        return True
    else:
        return False