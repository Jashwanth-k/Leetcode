class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def disHelper(word1, word2, i, j,dp):
            if i < 0 and j < 0:
                return 0
            if i < 0 and j >= 0:
                return j+1
            if j < 0 and i >= 0:
                return i+1
            if i < 0 or j < 0:
                return float('inf')
            
            if dp[i][j] != -1:
                return dp[i][j]

            if word1[i] == word2[j]:
                dp[i][j] = disHelper(word1, word2, i - 1, j - 1, dp)
                return dp[i][j]
            else:
                ins = disHelper(word1[:i+1] + word2[j], word2, i, j-1, dp)
                dele = disHelper(word1, word2, i - 1, j, dp)
                rep = disHelper(word1[:i] + word2[j] + word1[i + 1:], word2, i, j, dp)
                dp[i][j] = 1 + min(ins, dele, rep)
                return dp[i][j]

        n, m = len(word1), len(word2)
        dp = [[-1]*(m) for j in range(n)]
        return disHelper(word1, word2, n - 1, m - 1,dp)