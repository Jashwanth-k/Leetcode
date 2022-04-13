class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        ans = 1
        for i in arr:
            if i - difference in dp:
                dp[i] = dp[i-difference] + 1
            else:
                dp[i] = 1
            ans = max(ans,dp[i])
        return ans