class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[-1] * (m+1) for j in range(n+1)]
        for _ in range(n+1): dp[_][0] = 0
        for _ in range(m+1): dp[0][_] = 0

        for i in range(1, n+1):
            for j in range(1, m+1):
                ans1 = ans2 = ans3 = 0
                if text1[i-1] == text2[j-1]:
                    ans1 = 1 + dp[i - 1][j - 1]
                else:
                    ans2 = dp[i - 1][j]
                    ans3 = dp[i][j - 1]
                dp[i][j] = max(ans1, ans2, ans3)
        return dp[n][m]