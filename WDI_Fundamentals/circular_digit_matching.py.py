def get_first_two_digits(number):
    new_number = number
    while new_number >= 100:
        new_number = new_number // 10
    return new_number


def get_first_three_digits(number):
    new_number = number
    while new_number >= 1000:
        new_number = new_number // 10
    return new_number


def get_last_two_digits(number):
    return number % 100


def get_last_three_digits(number):
    return number % 1000


def calculate_glue_strength(a, b):

    if get_last_three_digits(a) == get_first_three_digits(b):
        return get_last_three_digits(a)
    elif get_last_two_digits(a) == get_first_two_digits(b):
        return get_last_two_digits(a)
    else:
        return 0


def find_max_glue_strength(arr):
    n = len(arr)
    if n == 0:
        return 0

    max_strength = 0
    current_strength = 0
    is_full_cycle = True

    for i in range(n):
        a = arr[i]
        b = arr[(i + 1) % n]
        current_glue = calculate_glue_strength(a, b)

        if current_glue > 0:
            current_strength += current_glue
        else:
            is_full_cycle = False
            if current_strength > max_strength:
                max_strength = current_strength
            current_strength = 0

    if current_strength > max_strength:
        max_strength = current_strength

    if is_full_cycle:
        return -1
    else:
        return max_strength
