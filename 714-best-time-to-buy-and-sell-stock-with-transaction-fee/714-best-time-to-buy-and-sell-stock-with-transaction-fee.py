class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0]*(2) for j in range(n+1)]

        for i in range(n-1,-1,-1):
            pick = -prices[i] + dp[i+1][0]
            unpick = dp[i+1][1]
            dp[i][1] = max(pick,unpick)
            
            sell = prices[i] - fee + dp[i+1][1]
            unsell = dp[i+1][0]
            dp[i][0] = max(sell,unsell)
        return dp[0][1] 