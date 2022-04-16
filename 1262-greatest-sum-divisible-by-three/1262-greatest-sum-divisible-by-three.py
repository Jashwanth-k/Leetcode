class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        def sumHelper(nums,i,total,dp):
            if i < 0:
                if total % 3 == 0:
                    return 0
                return float('-inf')
            
            if (i,total%3) in dp:
                return dp[i,total%3]
            
            pick = nums[i] + sumHelper(nums,i-1,total + nums[i],dp)
            unpick = sumHelper(nums,i-1,total,dp)
            dp[i,total % 3] = max(pick,unpick)
            return dp[i,total % 3]
            
        n = len(nums)
        dp = {}
        return sumHelper(nums,n-1,0,dp)