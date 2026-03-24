import math


def find_closest_divisors(n):
    min_difference = float("inf")
    best_i = 1
    best_j = n // best_i

    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            j = n // i
            current_diff = abs(i - j)

            if current_diff < min_difference:
                min_difference = current_diff
                best_i = i
                best_j = j

    return best_i, best_j