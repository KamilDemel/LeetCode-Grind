def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def simplify_fraction(fraction):
    num, den = fraction
    if den == 0: return (num, 0)
    if den < 0:
        den *= -1
        num *= -1
    common = gcd(abs(num), abs(den))
    return (num // common, den // common)


def find_longest_geometric_progression(arr):
    n = len(arr)
    if n < 2: return n

    a, b = arr[0]
    c, d = arr[1]

    if a != 0:
        current_ratio = simplify_fraction((c * b, d * a))
    else:
        current_ratio = (0, 1)

    max_length = 0
    current_length = 2

    for i in range(2, n):
        l, m = arr[i]
        g, s = arr[i - 1]

        if g == 0:
            current_length = 2
            if l != 0: current_ratio = (0, 1)
            continue

        ratio = simplify_fraction((l * s, m * g))

        if ratio == current_ratio:
            current_length += 1
            if current_length > max_length:
                max_length = current_length
        else:
            current_length = 2
            current_ratio = ratio

    return max_length