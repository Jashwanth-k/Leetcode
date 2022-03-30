class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def distinctHelper(s,t,i,j,dp):
            if j < 0:
                return 1
            if i < 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            
            ans1 = 0
            if s[i] == t[j]:
                ans1 = distinctHelper(s,t,i-1,j-1,dp)
            ans2 = distinctHelper(s,t,i-1,j,dp)
            dp[i][j] = ans1 + ans2
            return dp[i][j]
        
        n,m = len(s),len(t)
        dp = [[-1]*(m) for j in range(n)]
        return distinctHelper(s,t,n-1,m-1,dp)