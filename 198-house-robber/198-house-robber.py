class Solution:
    def robHelper(self,nums,i,dp,ans=float('-inf')):
        if i >= len(nums)-2:
            return nums[i]

        currans = float('-inf')
        for j in range(2, len(nums) - i):
            if dp[i+j] == -1:
                subans = self.robHelper(nums,i + j,dp)
                currans = max(subans,currans)
            else:
                currans = dp[i+j]
            ans = max(ans,currans)
        dp[i] = ans + nums[i]
        return dp[i]
    
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        ans = float('-inf')
        for i in range(len(nums)):
            currans = self.robHelper(nums,i,dp)
            ans = max(currans,ans)
        return ans
                