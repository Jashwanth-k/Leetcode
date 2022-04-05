class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def profitHelper(prices,i,k,buy,n,dp):
            if i == n or k == 0:
                return 0
            if dp[i][buy][k] != -1:
                return dp[i][buy][k]
            
            if buy == 1:
                pick = -prices[i] + profitHelper(prices,i+1,k,0,n,dp)
                unpick = profitHelper(prices,i+1,k,1,n,dp)
                dp[i][buy][k] = max(pick,unpick)
                return dp[i][buy][k]
            else:
                sell = prices[i] + profitHelper(prices,i+1,k-1,1,n,dp)
                unsell = profitHelper(prices,i+1,k,0,n,dp)
                dp[i][buy][k] = max(sell,unsell)
                return dp[i][buy][k]
        
        n = len(prices)
        dp = [[[-1]*(k+1) for j in range(2)] for i in range(n)]
        return profitHelper(prices,0,k,1,n,dp)