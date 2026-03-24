def is_prime(number):
    if number < 2:
        return False
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True


def validate_fibonacci_prime_condition(T, N):
    a, b = 0, 1
    first_condition = True
    second_condition = False
    for i in range(N):
        is_fibo_index = False
        while a <= i:
            if a == i:
                is_fibo_index = True
            a, b = b, a + b

        if is_fibo_index and is_prime(T[i]):
            first_condition = False

        if not is_fibo_index and is_prime(T[i]):
            second_condition = True

    return first_condition and second_condition