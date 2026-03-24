def get_unique_prime_factors(n):
    factors = set()
    d = 2
    temp = n
    while temp > 1:
        if temp % d == 0:
            factors.add(d)
            temp //= d
        else:
            d += 1
    return factors


def find_special_square(matrix):
    n = len(matrix)
    for k in range(1, n - 1):
        for r in range(n - k):
            for c in range(n - k):
                corner_product = (matrix[r][c] * matrix[r + k][c] * matrix[r][c + k] * matrix[r + k][c + k])
                unique_factors = get_unique_prime_factors(corner_product)
                if len(unique_factors) == 2:
                    return k + 1
    return 0