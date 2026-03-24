def get_gcd(a, b):
    if b == 0:
        return a
    return get_gcd(b, a % b)


def simplify_fraction(u1):
    l1, m1 = u1
    divisor = get_gcd(l1, m1)
    return (l1 // divisor, m1 // divisor)


def add_fractions(u1, u2):
    l1, m1, l2, m2 = u1[0], u1[1], u2[0], u2[1]
    return simplify_fraction((l1 * m2 + l2 * m1, m1 * m2))


def subtract_fractions(u1, u2):
    l1, m1, l2, m2 = u1[0], u1[1], u2[0], u2[1]
    return simplify_fraction((l1 * m2 - l2 * m1, m1 * m2))


def multiply_fractions(u1, u2):
    l1, m1, l2, m2 = u1[0], u1[1], u2[0], u2[1]
    return simplify_fraction((l1 * l2, m1 * m2))


def divide_fractions(u1, u2):
    l1, m1, l2, m2 = u1[0], u1[1], u2[0], u2[1]
    return simplify_fraction((l1 * m2, l2 * m1))


def solve_linear_system(A, B, C, D, E, F):

    W = subtract_fractions(multiply_fractions(A, D), multiply_fractions(B, C))
    if W[0] == 0:
        return None
    Wx = subtract_fractions(multiply_fractions(E, D), multiply_fractions(B, F))
    Wy = subtract_fractions(multiply_fractions(A, F), multiply_fractions(E, C))
    x = divide_fractions(Wx, W)
    y = divide_fractions(Wy, W)
    return x, y


def format_fraction(u1):
    l1, m1 = u1
    if m1 == 1: return str(l1)
    if l1 == 0: return "0"
    return f"{l1}/{m1}"