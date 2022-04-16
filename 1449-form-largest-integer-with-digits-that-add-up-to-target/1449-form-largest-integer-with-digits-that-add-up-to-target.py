class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        def number(cost,target,i,dp):
            if target == 0:
                return ""
            if i < 0:
                return "0"
            if (i,target) in dp:
                return dp[i,target]
            
            pick = "0"
            if cost[i] <= target:
                pick = number(cost,target-cost[i],i,dp)
            unpick = number(cost,target,i-1,dp)
            
            if pick != "0":
                pick = str(i+1) + pick
            dp[i,target] = pick if int(pick) > int(unpick) else unpick
            return dp[i,target]
        
        n = len(cost)
        dp = {}
        return number(cost,target,n-1,dp)