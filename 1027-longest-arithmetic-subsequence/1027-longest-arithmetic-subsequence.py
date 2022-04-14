class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [{} for j in range(n)]
        ans = 0
        
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                if diff in dp[j]:
                    dp[i][diff] = max(dp[j][diff]+1,2)
                else:
                    dp[i][diff] = 2
                ans = max(ans,dp[i][diff])
        return ans