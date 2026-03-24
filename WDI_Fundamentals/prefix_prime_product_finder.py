import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def find_max_prime_prefix_product_index(arr):
    n = len(arr)
    max_value = 0
    best_index = None

    for i in range(n):
        current_number = arr[i]
        prefix_product = 1

        for j in range(0, i):
            if is_prime(arr[j]):
                prefix_product *= arr[j]

        if current_number == prefix_product:
            if current_number > max_value:
                max_value = current_number
                best_index = i

    return best_index