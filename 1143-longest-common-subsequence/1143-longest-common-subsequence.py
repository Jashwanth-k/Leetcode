class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def lcsHelper(text1,text2,i,j,dp):
            if i < 0 or j < 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            
            ans1 = ans2 = ans3 = 0
            if text1[i] == text2[j]:
                ans1 = 1 + lcsHelper(text1,text2,i-1,j-1,dp)
            else:
                ans2 = lcsHelper(text1,text2,i-1,j,dp)
                ans3 = lcsHelper(text1,text2,i,j-1,dp)
            dp[i][j] = max(ans1,ans2,ans3)
            return dp[i][j]
        
        n,m = len(text1),len(text2)
        dp = [[-1]*(m+1) for j in range(n+1)]
        return lcsHelper(text1,text2,n-1,m-1,dp)