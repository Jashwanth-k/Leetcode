class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        def Helper(s, t, i, j, dp):
            if i < 0 or j < 0:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]

            if s[i] == t[j]:
                ans = 1 + Helper(s, t, i - 1, j - 1, dp)
            else:
                ans = Helper(s, t, i, j-1, dp)
            dp[i][j] = ans
            return ans

        n, m = len(s), len(t)
        dp = [[-1]*(m) for j in range(n)]
        return Helper(s, t, n - 1, m - 1, dp) == n