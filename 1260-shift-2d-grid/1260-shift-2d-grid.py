class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(grid),len(grid[0])        
        helper = []
        for i in grid:
            helper.extend(i)
        for _ in range(k):
            helper.insert(0,helper.pop())
        
        idx = 0
        for i in range(m):
            for j in range(n):
                grid[i][j] = helper[idx]
                idx += 1
        return grid