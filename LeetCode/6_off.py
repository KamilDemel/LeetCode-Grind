import sys
dane_wejsciowe = sys.stdin.read().split()
dane = iter(dane_wejsciowe)
q = int(next(dane))
dp = [1, 2, 7]
while True:
    nowy = (3 * dp[-1] + dp[-2] - dp[-3]) % 67
    dp.append(nowy)
    if dp[-3:] == [1, 2, 7]:
        dp = dp[:-3]
        break
dlugosc_cyklu = len(dp)
for _ in range(q):
    n = int(next(dane))
    print(dp[(n - 1) % dlugosc_cyklu])