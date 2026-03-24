def get_prime_factors(n):
    d = 2
    factors = set()
    temp = n
    while temp > 1:
        if temp % d == 0:
            factors.add(d)
            temp //= d
        else:
            d += 1
    return factors

def shares_exactly_one_prime(a, b):
    common = get_prime_factors(a) & get_prime_factors(b)
    return len(common) == 1

def count_special_neighbors(matrix):
    n = len(matrix)
    count = 0
    for r in range(1, n - 1):
        for c in range(1, n - 1):
            val = matrix[r][c]
            if (shares_exactly_one_prime(val, matrix[r+1][c]) and
                shares_exactly_one_prime(val, matrix[r][c+1]) and
                shares_exactly_one_prime(val, matrix[r-1][c]) and
                shares_exactly_one_prime(val, matrix[r][c-1])):
                count += 1
    return count