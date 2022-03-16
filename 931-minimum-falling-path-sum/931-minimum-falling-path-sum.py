class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1:
            return min(matrix[0])
        
        dp = [[float('inf')]*(n+1) for j in range(n+1)]
        ans = float('inf')
        for st in range(n-1,-1,-1):
            dp[n-1][st] = matrix[n-1][st]
            for i in range(n-2,-1,-1):
                for j in range(n-1,-1,-1):
                    curr = min(dp[i+1][j],dp[i+1][j+1],dp[i+1][j-1])
                    dp[i][j] = matrix[i][j] + curr
                    if i == 0:
                        ans = min(ans,dp[i][j])
            dp[n-1][st] = float('inf')
        return ans
                    