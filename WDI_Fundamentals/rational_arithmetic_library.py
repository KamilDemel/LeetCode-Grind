def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def simplify(fraction):
    num, den = fraction
    common_divisor = gcd(num, den)
    return (num // common_divisor, den // common_divisor)

def add_fractions(u1, u2):
    l1, m1 = u1
    l2, m2 = u2
    result = (l1 * m2 + l2 * m1, m1 * m2)
    return simplify(result)

def subtract_fractions(u1, u2):
    l1, m1 = u1
    l2, m2 = u2
    result = (l1 * m2 - l2 * m1, m1 * m2)
    return simplify(result)

def multiply_fractions(u1, u2):
    l1, m1 = u1
    l2, m2 = u2
    result = (l1 * l2, m1 * m2)
    return simplify(result)

def divide_fractions(u1, u2):
    l1, m1 = u1
    l2, m2 = u2
    result = (l1 * m2, l2 * m1)
    return simplify(result)

def power_fraction(u1, n):
    l1, m1 = u1
    res_l, res_m = 1, 1
    while n > 0:
        res_l *= l1
        res_m *= m1
        n -= 1
    return simplify((res_l, res_m))

def parse_fraction(text):
    slash_pos = text.find("/")
    if slash_pos == -1:
        return (int(text), 1)
    numerator = int(text[:slash_pos])
    denominator = int(text[slash_pos + 1:])
    return (numerator, denominator)

def format_fraction(u1):
    num, den = u1
    if den == 1:
        return str(num)
    if num == 0:
        return "0"
    return f"{num}/{den}"