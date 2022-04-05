class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def profitHelper(prices,i,buy,cool,n,dp):
            if i == n:
                return 0
            if dp[i][buy][cool] != -1:
                return dp[i][buy][cool]
            
            ans1 = ans2 = ans3 = float('-inf')
            if cool == 1:
                ans1 = profitHelper(prices,i+1,buy,0,n,dp)
            
            elif buy == 1:
                pick = -prices[i] + profitHelper(prices,i+1,0,cool,n,dp)
                unpick = profitHelper(prices,i+1,1,cool,n,dp)
                ans2 = max(pick,unpick)
            else:
                sell = prices[i] + profitHelper(prices,i+1,1,1,n,dp)
                unsell = profitHelper(prices,i+1,0,cool,n,dp)
                ans3 = max(sell,unsell)

            dp[i][buy][cool] = max(ans1,ans2,ans3)
            return dp[i][buy][cool]
        
        n = len(prices)
        dp = [[[-1]*(2) for j in range(2)] for i in range(n)]
        return profitHelper(prices,0,1,0,n,dp)
    