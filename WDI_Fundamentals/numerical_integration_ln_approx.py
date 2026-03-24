def approximate_ln(k, steps=1000000):
    width = (k - 1) / steps
    total_area = 0

    for i in range(steps):
        x = 1 + (i * width)
        height = 1 / x
        rectangle_area = width * height
        total_area += rectangle_area

    return total_area
