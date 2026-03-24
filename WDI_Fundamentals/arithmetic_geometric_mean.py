import math


def calculate_agm(start_a, start_b, iterations=10):
    a = start_a
    b = start_b

    for _ in range(iterations):
        arithmetic_mean = (a + b) / 2
        geometric_mean = math.sqrt(a * b)

        a = geometric_mean
        b = arithmetic_mean

    return a