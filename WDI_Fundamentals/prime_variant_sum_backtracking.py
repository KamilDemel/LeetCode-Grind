import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solve_prime_variant(arr):
    n = len(arr)
    target_sum = sum(arr)

    def backtrack(index, current_sum):
        if index == n:
            return current_sum == target_sum

        for offset in range(-2, 3):
            candidate = arr[index] + offset

            if candidate <= 20 and is_prime(candidate):
                if backtrack(index + 1, current_sum + candidate):
                    return True

        return False

    return backtrack(0, 0)