class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def targetHelper(nums,target,i,plus,minus,dp):
            if i < 0 and (plus + minus == target):
                return 1
            
            if i < 0:
                return 0
            
            if (i,plus + minus) in dp:
                return dp[i,plus + minus]
            
            add = targetHelper(nums,target,i-1,plus + nums[i],minus,dp)
            sub = targetHelper(nums,target,i-1,plus,minus - nums[i],dp)
            dp[i,plus + minus] = add + sub
            return dp[i,plus + minus]
        
        n,s = len(nums),sum(nums)
        dp = {}
        return targetHelper(nums,target,n-1,0,0,dp)
    