import math


def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)

    if limit >= 0:
        is_prime[0] = False
    if limit >= 1:
        is_prime[1] = False

    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    return is_prime


def find_prime_factors(number):
    factors = []

    primes_map = sieve_of_eratosthenes(number)

    for i in range(2, number):
        test_number = i
        if primes_map[test_number]:
            if number % test_number == 0:
                factors.append(test_number)

    return factors
