class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def lpsHelper(s, n, i, j, dp):
            if i >= n or j < 0 or i > j:
                return 0
            if dp[i][j] != -1: return dp[i][j]

            ans1 = ans2 = ans3 = 0
            if s[i] == s[j]:
                ct = 2
                if i == j: ct = 1
                ans1 = ct + lpsHelper(s, n, i + 1, j - 1, dp)
            else:
                ans2 = lpsHelper(s, n, i + 1, j, dp)
                ans3 = lpsHelper(s, n, i, j - 1, dp)
            dp[i][j] = max(ans1,ans2,ans3)
            return dp[i][j]

        n = len(s)
        dp = [[-1]*(n+1) for j in range(n+1)]
        return lpsHelper(s, n, 0, n - 1,dp)