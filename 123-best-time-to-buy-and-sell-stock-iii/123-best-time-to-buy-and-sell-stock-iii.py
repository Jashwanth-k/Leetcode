class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def profitHelper(prices, i, n, hold, maxPick,dp):
            if i == n or (maxPick >= 2 and hold == 1):
                return 0
            if (i,hold,maxPick) in dp:
                return dp[i,hold,maxPick]

            if hold == 1:
                pick = -prices[i] + profitHelper(prices, i + 1, n, 0, maxPick + 1,dp)
                unpick = profitHelper(prices, i + 1, n, 1, maxPick,dp)
                dp[i,hold,maxPick] = max(pick,unpick)
                return dp[i,hold,maxPick]
            else:
                sell = prices[i] + profitHelper(prices, i + 1, n, 1, maxPick,dp)
                unsell = profitHelper(prices, i + 1, n, 0, maxPick,dp)
                dp[i,hold,maxPick] = max(sell, unsell)
                return dp[i,hold,maxPick]

        n = len(prices)
        dp = {}
        return profitHelper(prices, 0, n, 1, 0,dp)