def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

x = 1/2
approx_result = 0

for n in range(0, 5):
    term = (((-1)**n) * (x**(2 * n))) / (factorial(2 * n))
    approx_result += term

