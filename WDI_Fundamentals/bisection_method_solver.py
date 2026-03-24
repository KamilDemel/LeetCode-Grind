def target_function(x):
    result = x ** x - 2024
    return result


if __name__ == "__main__":
    a = 0
    b = 5
    precision = 0.0001

    while a <= b:
        midpoint = (a + b) / 2

        if target_function(midpoint) < 0:
            a = midpoint
        else:
            b = midpoint

        if b - a < precision:
            print(f"Root found: {midpoint}")
            break