class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        def DFS(grid,i,j,n,m,k):
            if i >= n or j >= m:
                return False
            if grid[i][j] == "(":  k += 1
            else:  k -= 1
            if k < 0:
                return False
            if i == n-1 and j == m-1:
                return k == 0
            if (i,j,k) in self.dp:
                return self.dp[i,j,k]
            
            right = DFS(grid,i,j+1,n,m,k)
            down = DFS(grid,i+1,j,n,m,k)
            self.dp[i,j,k] = right or down
            return right or down
        
        n,m = len(grid),len(grid[0])
        self.dp = {}
        if grid[0][0] == ")" or grid[-1][-1] == "(":  return False
        return DFS(grid,0,0,n,m,0)