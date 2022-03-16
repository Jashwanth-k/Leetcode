class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def uniquePathsHelper(grid,m,n,i,j,dp):
            if i >= m or j >= n or grid[i][j] == 1:
                return 0
            
            if i == m-1 and j == n-1:
                return 1
            
            if dp[i][j] != -1: return dp[i][j]
            
            right = uniquePathsHelper(grid,m,n,i,j+1,dp)
            down = uniquePathsHelper(grid,m,n,i+1,j,dp)
            dp[i][j] = right+down
            return dp[i][j] 
        
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        dp = [[-1]*n for i in range(m)]
        return uniquePathsHelper(obstacleGrid,m,n,0,0,dp)