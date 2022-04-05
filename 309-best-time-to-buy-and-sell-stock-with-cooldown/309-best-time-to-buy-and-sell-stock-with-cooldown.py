class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def profitHelper(prices,i,buy,n,dp):
            if i >= n:
                return 0
            if dp[i][buy] != -1:
                return dp[i][buy]
            
            ans1 = ans2 = float('-inf')
            if buy == 1:
                pick = -prices[i] + profitHelper(prices,i+1,0,n,dp)
                unpick = profitHelper(prices,i+1,1,n,dp)
                ans1 = max(pick,unpick)
            else:
                sell = prices[i] + profitHelper(prices,i+2,1,n,dp)
                unsell = profitHelper(prices,i+1,0,n,dp)
                ans2 = max(sell,unsell)

            dp[i][buy] = max(ans1,ans2)
            return dp[i][buy]
        
        n = len(prices)
        dp = [[-1]*(2) for i in range(n)]
        return profitHelper(prices,0,1,n,dp)
    