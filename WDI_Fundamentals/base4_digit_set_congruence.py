def get_base4_digit_set(number):
    base = 4
    digits = set()
    if number == 0:
        digits.add(0)
    while number > 0:
        remainder = number % base
        digits.add(remainder)
        number //= base
    return digits


def share_same_digit_set(num1, num2):
    return get_base4_digit_set(num1) == get_base4_digit_set(num2)


def find_max_congruent_group(arr):
    n = len(arr)
    max_count = 1

    for i in range(n):
        reference_num = arr[i]
        current_group_size = 1
        for j in range(i + 1, n):
            if share_same_digit_set(reference_num, arr[j]):
                current_group_size += 1

        if current_group_size > max_count:
            max_count = current_group_size

    return max_count