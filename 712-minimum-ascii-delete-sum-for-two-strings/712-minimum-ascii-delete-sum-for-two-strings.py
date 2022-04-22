class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n,m = len(s1),len(s2)
        dp = [[0]*(m+1) for j in range(n+1)]
        
        for k in range(1,m+1):
            dp[0][k] = ord(s2[k-1]) + dp[0][k-1]
        for k in range(1,n+1):
            dp[k][0] = ord(s1[k-1]) + dp[k-1][0]
            
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    ans1 = ord(s2[j-1]) + dp[i][j-1]
                    ans2 = ord(s1[i-1]) + dp[i-1][j]
                    dp[i][j] = min(ans1,ans2)
        return dp[n][m]