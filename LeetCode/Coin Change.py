class Solution(object):
    def coinChange(self, coins, amount):
        memo = {}
        def reku_pomoc_top_down(rem_amount=amount):
            if rem_amount in memo:
                return memo[rem_amount]
            if rem_amount == 0:
                return 0
            if rem_amount < 0:
                return float("inf")
            najlepsza_opcja = float("inf")
            for coin in coins:
                if rem_amount - coin >= 0:
                    koszt = 1 + reku_pomoc_top_down(rem_amount-coin)
                    najlepsza_opcja = min(najlepsza_opcja,koszt)
            memo[rem_amount] = najlepsza_opcja
            return najlepsza_opcja
        wynik = reku_pomoc_top_down()
        if wynik == float("inf"):
            return -1
        return wynik
class Solution2(object):
    def coinChange_bottom_up(self, coins, amount):
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i],1 + dp[i - coin])
        if dp[amount] == float("inf"):
            return -1
        return dp[amount]