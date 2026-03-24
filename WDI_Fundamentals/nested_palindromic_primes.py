def sieve(limit):
    table = [True] * (limit + 1)
    table[0] = table[1] = False
    i = 2
    while i * i <= limit:
        if table[i]:
            for j in range(i * i, limit + 1, i):
                table[j] = False
        i += 1
    return table


def is_palindrome(text):
    return text == text[::-1]


def peel_number(text):
    if len(text) <= 2:
        return ""
    else:
        return text[1:-1]


limit = int(input("Enter limit: "))
prime_map = sieve(limit)

for i in range(2, limit):
    current_val = i
    is_super_prime = True

    while True:
        s_val = str(current_val)

        if not prime_map[current_val]:
            is_super_prime = False
            break
        if not is_palindrome(s_val):
            is_super_prime = False
            break

        if len(s_val) <= 1:
            break

        peeled = peel_number(s_val)
        if peeled == "":
            break

        current_val = int(peeled)

    if is_super_prime:
        print(f"Found: {i}")



