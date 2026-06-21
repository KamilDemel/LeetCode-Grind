import heapq
def kstrong(T, k):
    n = len(T)
    dp = [[float('-inf')] * (k + 1) for _ in range(n)]
    dp[0][0] = T[0]
    najlepszy_max = T[0]
    for i in range(1, n):
        for j in range(k + 1):
            bierzemy = T[i]
            if dp[i - 1][j] != float('-inf'):
                bierzemy = max(bierzemy, dp[i - 1][j] + T[i])
            usuwamy = float('-inf')
            if j > 0 and dp[i - 1][j - 1] != float('-inf'):
                usuwamy = dp[i - 1][j - 1]
            dp[i][j] = max(bierzemy, usuwamy)
            if dp[i][j] > najlepszy_max:
                najlepszy_max = dp[i][j]
    return najlepszy_max

def brute_force_k_strong(T, k):
    lista_tab = []
    for i in range(len(T)):
        for j in range(i+1,len(T)+1):
            new_tab = T[i:j]
            sorted_T = sorted(new_tab)
            lista_tab.append(sorted_T)
    best_suma = float("-inf")
    for tab in lista_tab:
        usunieto = 0
        while usunieto <= k:
            suma = sum(tab[usunieto:])
            if suma > best_suma:
                best_suma = suma
            usunieto += 1
    return best_suma
def heap_soluton_k_strong(T,k):
    left = 0
    max_suma = float("-inf")
    while left < len(T):
        akt_suma = 0
        right = left
        pq = []
        while right < len(T):
            akt_suma += T[right]
            if T[right] < 0:
                heapq.heappush(pq,-T[right])
                akt_suma -= T[right]
            if len(pq) > k:
                akt_suma += -(heapq.heappop(pq))
            if akt_suma > max_suma:
                max_suma = akt_suma
            right += 1
        left += 1
    return max_suma






