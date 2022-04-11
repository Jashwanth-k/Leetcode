class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(grid),len(grid[0])        
        for _ in range(k):
            for i in range(m):
                for j in range(n):
                    if i == j == 0:
                        prev = grid[i][j]
                        grid[i][j] = grid[m-1][n-1]
                    else:
                        curr = grid[i][j]
                        grid[i][j] = prev
                        prev = curr
        return grid