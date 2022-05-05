class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        def cherryPaths(grid,i1,j1,i2,j2,n,dp):
            if (i1 == n - 1 and j1 == n - 1) or (i2 == n - 1 and j2 == n - 1):
                return grid[n - 1][n - 1]       
            if (i1,i2,j1,j2) in dp:
                return dp[i1,i2,j1,j2]

            paths1 = [[i1, j1 + 1], [i1 + 1, j1]]
            paths2 = [[i2, j2 + 1], [i2 + 1, j2]]            
            ans = float('-inf')
            for r1, c1 in paths1:
                for r2, c2 in paths2:
                    if r1 < n and c1 < n and r2 < n and c2 < n:
                        if grid[r1][c1] != -1 and grid[r2][c2] != -1:
                            curr = cherryPaths(grid, r1, c1, r2, c2, n, dp)
                            ans = max(curr,ans)
  
            if i1 == i2 and j1 == j2:
                dp[i1,i2,j1,j2] = grid[i1][j1] + ans
            else:
                dp[i1,i2,j1,j2] = grid[i1][j1] + grid[i2][j2] + ans                
            return dp[i1,i2,j1,j2]
            
        n = len(grid)
        dp = {}
        output = cherryPaths(grid,0,0,0,0,n,dp)
        return 0 if output == float('-inf') else output
        