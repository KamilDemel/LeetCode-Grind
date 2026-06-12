def get_prefix_xor(x):
    reszta = x % 4
    if reszta == 0:
        return x
    elif reszta == 1:
        return 1
    elif reszta == 2:
        return x + 1
    else:
        return 0
def solve(n, K):
    L = 1 + K
    R = n + K
    xor_range = get_prefix_xor(R) ^ get_prefix_xor(L - 1)
    wynik = xor_range - K
    return wynik
n, K = map(int, input().split())
print(solve(n,K))