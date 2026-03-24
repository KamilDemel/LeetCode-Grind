import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_max_prime_ratio(arr):
    n = len(arr)
    max_ratio = 0

    for i in range(n):
        for j in range(i + 1, n):
            length = j - i + 1

            if length == n:
                continue

            sum_a = 0
            for k in range(0, length - 1, 2):
                sum_a += arr[i + k] * arr[i + k + 1]
            if length % 2 != 0:
                sum_a += arr[i + length - 1]

            sum_b = arr[i]
            for k in range(1, length - 1, 2):
                sum_b += arr[i + k] * arr[i + k + 1]
            if length % 2 == 0:
                sum_b += arr[i + length - 1]

            for current_sum in [sum_a, sum_b]:
                if is_prime(current_sum):
                    ratio = current_sum / length
                    if ratio > max_ratio:
                        max_ratio = ratio

    return max_ratio