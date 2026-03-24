def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def reverse_array(arr, length):
    left = 0
    right = length - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


def convert_to_base_array(number, base, result_array):
    count = 0
    while number > 0:
        remainder = number % base
        result_array[count] = remainder
        number = number // base
        count += 1
    reverse_array(result_array, count)
    return count


def array_slice_to_int(digit_array, start, stop, base):
    result_10 = 0
    for i in range(start, stop):
        digit = digit_array[i]
        result_10 = (result_10 * base) + digit
    return result_10


def find_best_base_split(n):
    best_base = 0
    best_product = 0

    max_digits = 100
    digit_array = [0] * max_digits

    for current_base in range(2, 17):
        length = convert_to_base_array(n, current_base, digit_array)

        for split_point in range(1, length):
            left_number = array_slice_to_int(digit_array, 0, split_point, current_base)
            right_number = array_slice_to_int(digit_array, split_point, length, current_base)

            if get_gcd(left_number, right_number) == 1:
                product = left_number * right_number
                if product > best_product:
                    best_product = product
                    best_base = current_base

    return best_base