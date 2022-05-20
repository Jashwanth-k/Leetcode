class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n,m = len(obstacleGrid),len(obstacleGrid[0])
        dp = [[0]*m for j in range(n)]
            
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if obstacleGrid[i][j] == 1:
                    continue
                if i == n-1 and j == m-1:
                    dp[i][j] = 1
                    continue
                
                ans1 = dp[i][j+1] if j + 1 < m else 0
                ans2 = dp[i+1][j] if i + 1 < n else 0
                dp[i][j] = ans1 + ans2
        return dp[0][0]