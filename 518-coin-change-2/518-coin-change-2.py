class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for j in range(n)]

        for i in range(n): dp[i][0] = 1
        for i in range(n):
            for target in range(1, amount + 1):
                inclu = 0
                if target >= coins[i]:
                    inclu = dp[i][target - coins[i]]
                exclu = dp[i - 1][target]
                dp[i][target] = inclu + exclu
        return dp[-1][-1]
