def convert_to_base(number, base):
    if number == 0:
        return "0"
    digits_map = "0123456789ABCDEF"
    remainders = []
    temp = number
    while temp > 0:
        remainder = temp % base
        remainders.append(digits_map[remainder])
        temp //= base
    result = "".join(remainders[::-1])
    return result