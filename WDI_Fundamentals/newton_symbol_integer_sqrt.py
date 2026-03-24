def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    n = int(input("Enter n: "))
    k = int(input("Enter k: "))

    if k > n or k < 0:
        print("Please enter k in the range from 0 to n")
    else:
        newton_symbol = factorial(n) // (factorial(k) * factorial(n - k))

        result = 0
        current_odd = 1

        while newton_symbol >= current_odd:
            newton_symbol -= current_odd
            result += 1
            current_odd += 2

        print(f"Result (integer sqrt of Newton symbol): {result}")