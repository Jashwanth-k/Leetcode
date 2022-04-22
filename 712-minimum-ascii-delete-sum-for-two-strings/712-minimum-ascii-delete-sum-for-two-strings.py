class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        def lcs(s1,s2,i,j,dp):
            if i < 0 and j < 0:
                return 0
            if i < 0:
                curr = 0
                for k in s2[:j+1]:
                    curr += ord(k)
                return curr
            if j < 0:
                curr = 0
                for k in s1[:i+1]:
                    curr += ord(k)
                return curr
            if dp[i][j] != -1:
                return dp[i][j]
            
            if s1[i] == s2[j]:
                dp[i][j] = lcs(s1,s2,i-1,j-1,dp)
                return dp[i][j]
            else:
                ans1 = ord(s2[j]) + lcs(s1,s2,i,j-1,dp)
                ans2 = ord(s1[i]) + lcs(s1,s2,i-1,j,dp)
                dp[i][j] = min(ans1,ans2)
                return dp[i][j]
            
        n,m = len(s1),len(s2)
        dp = [[-1]*(m) for j in range(n)]
        return lcs(s1,s2,n-1,m-1,dp)