def to_octal(number):
    system = 8
    result = 0
    multiplier = 1
    while number > 0:
        remainder = number % system
        result = result + (remainder * multiplier)
        number = number // system
        multiplier = multiplier * 10
    return result


def has_unique_digits(number):
    digits_list = []
    while number > 0:
        last_digit = number % 10
        if last_digit not in digits_list:
            digits_list.append(last_digit)
        else:
            return False
        number = number // 10
    return True


def satisfies_condition(number):
    octal_num = to_octal(number)
    return has_unique_digits(octal_num)


def find_max_square(matrix):
    n = len(matrix)
    logic_table = [[0] * n for _ in range(n)]

    # Building the logic table
    for i in range(n):
        for j in range(n):
            if satisfies_condition(matrix[i][j]):
                logic_table[i][j] = 1
            else:
                logic_table[i][j] = 0

    max_side = 0
    for i in range(n):
        for j in range(n):
            side = 0
            if logic_table[i][j] == 0:
                continue
            else:
                side += 1
                while i + side < n and j + side < n:
                    is_ok = True
                    for k in range(side + 1):
                        if logic_table[i + side][j + k] != 1 or logic_table[i + k][j + side] != 1:
                            is_ok = False
                            break
                    if is_ok:
                        side += 1
                    else:
                        break
            if side > max_side:
                max_side = side
    return max_side