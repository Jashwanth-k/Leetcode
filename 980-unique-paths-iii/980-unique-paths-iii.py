class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def uniquePaths(grid,r,c,n,m,ct):
            if grid[r][c] == -1:
                return 0
            if grid[r][c] == 2:
                return 1 if ct == 0 else 0
            
            paths = [[r,c+1],[r,c-1],[r+1,c],[r-1,c]]
            ans = 0
            curr = grid[r][c]
            grid[r][c] = -1
            
            for i,j in paths:
                if 0 <= i < n and 0 <= j < m:
                    ans += uniquePaths(grid,i,j,n,m,ct-1)
            grid[r][c] = curr
            return ans
            
        n,m = len(grid),len(grid[0])
        obscount = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    si,ei = i,j
                elif grid[i][j] == -1:
                    obscount += 1
        total = n*m
        ct = total - obscount - 1
        return uniquePaths(grid,si,ei,n,m,ct)