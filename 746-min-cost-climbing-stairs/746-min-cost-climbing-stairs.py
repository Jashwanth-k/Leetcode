class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def minCost(n,cost,dp):
            if n >= len(cost):
                return 0
            
            if dp[n+1] == -1:
                ans1 = minCost(n+1,cost,dp)
                dp[n+1] = ans1
            else:
                ans1 = dp[n+1]
                
            if dp[n+2] == -1:
                ans2 = minCost(n+2,cost,dp)
                dp[n+2] = ans2
            else:
                ans2 = dp[n+2]
            return cost[n] + min(ans1,ans2)
        
        return min(minCost(0,cost,[-1] * (len(cost)+2)),minCost(1,cost,[-1] * (len(cost)+2)))