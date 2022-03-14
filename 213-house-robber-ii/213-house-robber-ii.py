class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def robHelper(nums,i):
            if i == 0:
                return nums[i]
            if i < 0:
                return 0
            
            if dp[i] != -1: return dp[i]
            
            pick = nums[i] + robHelper(nums,i-2)
            unpick = robHelper(nums,i-1)
            dp[i] = max(pick,unpick)
            return dp[i]
        
        n = len(nums)
        dp = [-1] * n
        ans1 = robHelper(nums[:-1],n-2)
        dp = [-1] * n
        ans2 = robHelper(nums[1:],n-2)
        return max(ans1,ans2)