class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def profitHelper(prices,i,buy,n,dp):
            if i == n:
                return 0
            if dp[i][buy] != -1:
                return dp[i][buy]
            
            if buy == 0:
                pick = -prices[i] + profitHelper(prices,i+1,1,n,dp)
                unpick = profitHelper(prices,i+1,0,n,dp)
                dp[i][buy] = max(pick,unpick)
                return dp[i][buy]
            else:
                pick = prices[i] + profitHelper(prices,i+1,0,n,dp)
                unpick = profitHelper(prices,i+1,1,n,dp)
                dp[i][buy] = max(pick,unpick)
                return dp[i][buy]
            
        n = len(prices)
        dp = [[-1]*2 for i in range(n)]
        return profitHelper(prices,0,0,n,dp)