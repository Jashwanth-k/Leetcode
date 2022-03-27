class Solution:
    def minInsertions(self, s: str) -> int:
        def lps(s,i,j,dp):
            if i > j:
                return 0
            if dp[i][j] != -1: return dp[i][j]
            
            ans1 = ans2 = ans3 = 0
            if s[i] == s[j]:
                ct = 2
                if i == j: ct = 1
                ans1 = ct + lps(s,i+1,j-1,dp)
            else:
                ans2 = lps(s,i+1,j,dp)
                ans3 = lps(s,i,j-1,dp)
            dp[i][j] = max(ans1,ans2,ans3)
            return dp[i][j]
                    
        n = len(s)
        dp = [[-1]*(n+1) for j in range(n+1)]
        return n - lps(s,0,n-1,dp)