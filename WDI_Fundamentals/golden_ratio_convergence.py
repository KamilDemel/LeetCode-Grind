def calculate_limit_ratio(start_a, start_b, steps=40):
    a = start_a
    b = start_b
    last_ratio = 0.0

    if a == 0 and b == 0:
        return 0
    else:
        for _ in range(steps):
            if a != 0:
                last_ratio = b / a
            a, b = b, a + b

    return last_ratio
