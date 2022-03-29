class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def lcs(word1,word2,i,j,dp):
            if i < 0 or j < 0:
                return 0
            if dp[i][j] != -1: return dp[i][j]
            
            ans1 = ans2 = ans3 = 0
            if word1[i] == word2[j]:
                ans1 = 2 + lcs(word1,word2,i-1,j-1,dp)
            else:
                ans2 = lcs(word1,word2,i-1,j,dp)
                ans3 = lcs(word1,word2,i,j-1,dp)
            dp[i][j] = max(ans1,ans2,ans3)
            return dp[i][j]
                
        n,m = len(word1),len(word2)
        dp = [[-1]*(m) for j in range(n)]
        return n+m - lcs(word1,word2,n-1,m-1,dp)