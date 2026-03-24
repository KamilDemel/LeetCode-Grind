from decimal import Decimal, getcontext


def calculate_euler_constant(precision=1000):
    getcontext().prec = precision + 3

    e_sum = Decimal(1)
    current_term = Decimal(1)

    for i in range(1, 500):
        current_term /= Decimal(i)
        e_sum += current_term

    return e_sum