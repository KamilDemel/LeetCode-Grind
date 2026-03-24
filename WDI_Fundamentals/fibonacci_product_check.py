if __name__ == "__main__":
    n = int(input("Enter n: "))

    a = 0
    b = 1
    is_product = False

    if n == 0:
        is_product = True
    else:
        while a * b < n:
            a, b = b, a + b
            if a * b == n:
                is_product = True
                break

    if is_product:
        print("YES")
    else:
        print("NO")



