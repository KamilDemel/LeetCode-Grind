def is_palindrome_iterative(number):
    text = str(number)
    start = 0
    end = len(text) - 1
    while start < end:
        if text[start] != text[end]:
            return False
        else:
            start += 1
            end -= 1
    return True

def convert_to_binary_as_int(number):
    base = 2
    result = 0
    multiplier = 1
    while number > 0:
        result = result + (number % base) * multiplier
        number = number // base
        multiplier = multiplier * 10
    return result

n = int(input("Enter number: "))

if is_palindrome_iterative(n):
    print("Decimal: YES")
else:
    print("Decimal: NO")

binary_rep = convert_to_binary_as_int(n)
if is_palindrome_iterative(binary_rep):
    print("Binary: YES")
else:
    print("Binary: NO")