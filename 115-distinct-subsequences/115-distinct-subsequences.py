class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m = len(s),len(t)
        dp = [0]*(m+1)
        dp[0] = 1
        
        for i in range(1,n+1):
            for j in range(m,0,-1):
                ans1 = 0
                if s[i-1] == t[j-1]:
                    ans1 = dp[j-1]
                ans2 = dp[j]
                dp[j] = ans1 + ans2
        return dp[m]