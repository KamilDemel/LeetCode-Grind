import sys

MOD = 10 ** 9 + 696969
MAX_K = 50005

fact = [1] * MAX_K
inv_fact = [1] * MAX_K

fact[0] = 1
for i in range(1, MAX_K):
    fact[i] = (fact[i - 1] * i) % MOD

inv_fact[MAX_K - 1] = pow(fact[MAX_K - 1], MOD - 2, MOD)
for i in range(MAX_K - 2, -1, -1):
    inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD


def nCr(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD


inputt = sys.stdin.read().split()
if not inputt:
    sys.exit(0)
dane = iter(inputt)

n = int(next(dane))
m = int(next(dane))
A = int(next(dane))
B = int(next(dane))
q = int(next(dane))

dp_X = [[0] * (n + 1) for _ in range(n + 1)]
dp_X[0][0] = 1
for k in range(1, n + 1):
    suma_okna = 0
    for x in range(n + 1):
        if x > 0:
            suma_okna = (suma_okna + dp_X[k - 1][x - 1]) % MOD
        if x > A:
            suma_okna = (suma_okna - dp_X[k - 1][x - A - 1] + MOD) % MOD
        dp_X[k][x] = suma_okna

dp_Y = [[0] * (m + 1) for _ in range(m + 1)]
dp_Y[0][0] = 1
for k in range(1, m + 1):
    suma_okna = 0
    for y in range(m + 1):
        if y > 0:
            suma_okna = (suma_okna + dp_Y[k - 1][y - 1]) % MOD
        if y > B:
            suma_okna = (suma_okna - dp_Y[k - 1][y - B - 1] + MOD) % MOD
        dp_Y[k][y] = suma_okna

for _ in range(q):
    K = int(next(dane))
    cel_x = int(next(dane))
    cel_y = int(next(dane))

    dx = cel_x - 1
    dy = cel_y - 1

    if dx < 0 or dy < 0 or dx > n or dy > m:
        print(0)
        continue

    total_ways = 0

    min_kx = (dx + A - 1) // A if dx > 0 else 0
    min_ky = (dy + B - 1) // B if dy > 0 else 0

    for k_x in range(min_kx, dx + 1):
        val_x = dp_X[k_x][dx]
        if val_x == 0:
            continue

        for k_y in range(min_ky, dy + 1):
            if k_x + k_y > K:
                break

            val_y = dp_Y[k_y][dy]
            if val_y == 0:
                continue

            kombinacje = nCr(K, k_x) * nCr(K - k_x, k_y) % MOD
            wariant = kombinacje * val_x % MOD * val_y % MOD
            total_ways = (total_ways + wariant) % MOD

    print(total_ways)