class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[-1]*(m+1) for j in range(n+1)]
        dp[0][0] = 0
        for k in range(1,m+1):
            dp[0][k] = k
        for k in range(1,n+1):
            dp[k][0] = k
            
        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    ins = dp[i][j-1]
                    dele = dp[i-1][j]
                    rep = dp[i-1][j-1]
                    dp[i][j] = 1 + min(ins, dele, rep)
        return dp[n][m]