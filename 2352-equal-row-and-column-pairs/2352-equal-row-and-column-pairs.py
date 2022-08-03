class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        res = 0
        for i in range(n):
            cur = [0]*n
            for j in range(n):
                cur[j] = grid[j][i]
            for k in range(n):
                if cur == grid[k]:
                    res += 1
        return res