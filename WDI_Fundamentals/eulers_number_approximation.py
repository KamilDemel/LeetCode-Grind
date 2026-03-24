def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

approx_e = 0
for i in range(20):
    approx_e = approx_e + 1 / factorial(i)