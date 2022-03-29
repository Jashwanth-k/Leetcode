class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n,m = len(word1),len(word2)
        dp = [[0]*(m+1) for j in range(n+1)]
        
        output = float('-inf')
        for i in range(1,n+1):
            for j in range(1,m+1):
                ans1 = ans2 = ans3 = 0
                if word1[i-1] == word2[j-1]:
                    ans1 = 2 + dp[i-1][j-1]
                else:
                    ans2 = dp[i-1][j]
                    ans3 = dp[i][j-1]
                dp[i][j] =  max(ans1,ans2,ans3)
                output = max(dp[i][j],output)
        return n+m - output