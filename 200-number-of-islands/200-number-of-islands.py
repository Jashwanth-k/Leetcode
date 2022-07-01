class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def DFS(r,c):
            visited.add((r,c))
            paths = [[r,c+1],[r,c-1],[r+1,c],[r-1,c]]
            for i,j in paths:
                if 0 <= i < m and 0 <= j < n and grid[i][j] == "1" and (i,j) not in visited:
                    DFS(i,j)
                    
        m,n = len(grid),len(grid[0])
        visited = set()
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0" or (i,j) in visited: continue
                DFS(i,j)
                ans += 1
        return ans  