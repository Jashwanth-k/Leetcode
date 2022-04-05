class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        def profitHelper(prices,fee,i,buy,n,dp):
            if i == n:
                return 0
            
            if dp[i][buy] != -1:
                return dp[i][buy]
            
            if buy == 1:
                pick = -prices[i] + profitHelper(prices,fee,i+1,0,n,dp)
                unpick = profitHelper(prices,fee,i+1,1,n,dp)
                dp[i][buy] = max(pick,unpick)
                return dp[i][buy]
            else:
                sell = prices[i] - fee + profitHelper(prices,fee,i+1,1,n,dp)
                unsell = profitHelper(prices,fee,i+1,0,n,dp)
                dp[i][buy] = max(sell,unsell)
                return dp[i][buy]
                
        n = len(prices)
        dp = [[-1]*(2) for j in range(n)]
        return profitHelper(prices,fee,0,1,n,dp)