class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        def ballHelper(grid,i,j,n,m,dp):
            if i == n:
                return j
            
            if grid[i][j] == 1 and j + 1 >= m:
                return -1
            if grid[i][j] == -1 and j - 1 < 0:
                return -1 
            if grid[i][j] == 1 and grid[i][j+1] == -1:
                return -1
            if grid[i][j] == -1 and grid[i][j-1] == 1:
                return -1
            
            if dp[i][j] != -2:
                return dp[i][j]
            
            right = left = float('-inf')
            if grid[i][j] == 1:
                right = ballHelper(grid,i+1,j+1,n,m,dp)
            if grid[i][j] == -1:
                left = ballHelper(grid,i+1,j-1,n,m,dp)
                
            dp[i][j] = max(left,right)
            return dp[i][j]
        
        n,m = len(grid),len(grid[0])
        output = []
        dp = [[-2]*(m) for j in range(n)]
        for k in range(m):
            ans = ballHelper(grid,0,k,n,m,dp)
            output.append(ans)
        return output
                