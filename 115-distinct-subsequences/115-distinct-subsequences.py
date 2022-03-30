class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m = len(s),len(t)
        dp = [[0]*(m+1) for j in range(n+1)]
        for k in range(n+1):
            dp[k][0] = 1
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                ans1 = 0
                if s[i-1] == t[j-1]:
                    ans1 = dp[i-1][j-1]
                ans2 = dp[i-1][j]
                dp[i][j] = ans1 + ans2
        return dp[n][m]