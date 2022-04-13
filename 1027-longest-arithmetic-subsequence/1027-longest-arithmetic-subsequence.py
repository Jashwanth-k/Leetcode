class Solution:
    def helper(self,nums,diff):
        dp = {}
        ans = 1
        for i in nums:
            if i - diff in dp:
                dp[i] = dp[i - diff] + 1
            else:
                dp[i] = 1
            ans = max(ans,dp[i]) 
        return ans
    
    def longestArithSeqLength(self, nums: List[int]) -> int:
        limit = max(nums) - min(nums)
        output = 1
        for j in range(limit+1):
            ans1 = self.helper(nums,j)
            ans2 = self.helper(nums,-j)
            output = max(ans1,ans2,output)
        return output