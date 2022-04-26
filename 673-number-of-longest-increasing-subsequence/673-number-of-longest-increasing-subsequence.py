class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        count = [1] * n
        ans = 1

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if 1 + dp[j] > dp[i]:
                        dp[i] = 1 + dp[j]
                        count[i] = count[j]
                    elif 1 + dp[j] == dp[i]:
                        count[i] += count[j]
            ans = max(ans,dp[i])

        output = 0
        for i in range(n):
            if dp[i] == ans:
                output += count[i]
        return output
                    