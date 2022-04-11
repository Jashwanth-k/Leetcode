class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n,m = len(grid),len(grid[0])
        
        def DFS(grid,r,c):
            col = grid[r][c]
            nextcol = col + c
        
            if nextcol >= m or nextcol < 0:
                return -1
            if col == 1 and grid[r][c] != grid[r][c+1]:
                return -1
            if col == -1 and grid[r][c] != grid[r][c-1]:
                return -1
            if r == n-1:
                return nextcol
            return DFS(grid,r+1,nextcol)
        
        output = []
        for i in range(m):
            ans = DFS(grid,0,i)
            output.append(ans)
        return output