class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def minPathHelper(grid,m,n,i,j,dp):
            if i == m-1 and j == n-1:
                return grid[i][j]
            
            if i >= m or j >= n:
                return float('inf')
            
            if dp[i][j] != -1: return dp[i][j]
            
            right = minPathHelper(grid,m,n,i,j+1,dp)
            down = minPathHelper(grid,m,n,i+1,j,dp)
            dp[i][j] = grid[i][j] + min(right,down)
            return dp[i][j]
        
        m,n = len(grid),len(grid[0])
        dp = [[-1]*n for i in range(m)]
        return minPathHelper(grid,m,n,0,0,dp)