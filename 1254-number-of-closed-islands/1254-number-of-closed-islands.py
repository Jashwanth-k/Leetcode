class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def DFS(r,c):
            if r < 0 or c < 0 or r >= m or c >= n:
                self.check = False
                return
            if grid[r][c] == 1 or grid[r][c] == "#":
                return 
            grid[r][c] = "#"
            DFS(r,c+1)
            DFS(r,c-1)
            DFS(r+1,c)
            DFS(r-1,c)
            
        m,n = len(grid),len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 or grid[i][j] == "#": continue
                self.check = True
                DFS(i,j)
                if self.check: ans += 1
        return ans