import sys
sys.setrecursionlimit(100000)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def coinHelper(coins,amount,dp,i):
            if amount == 0:
                return 0

            if i < 0:
                return float('inf')

            if dp[i][amount] != -1:
                return dp[i][amount]

            inclu = float('inf')
            if coins[i] <= amount:
                inclu = 1 + coinHelper(coins, amount - coins[i], dp, i)
            exclu = coinHelper(coins, amount, dp, i - 1)
            
            dp[i][amount] = min(inclu, exclu)
            return dp[i][amount]
        
        n = len(coins)
        dp = [[-1]*(amount+1) for j in range(n)]
        ans = coinHelper(coins,amount,dp,n-1)
        return -1 if ans == float('inf') else ans