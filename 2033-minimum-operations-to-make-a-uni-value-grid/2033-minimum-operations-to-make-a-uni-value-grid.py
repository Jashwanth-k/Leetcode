class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        n,m = len(grid),len(grid[0])
        helper = []
        for i in grid:
            helper.extend(i)
        helper.sort()
        midEle = helper[(n*m)//2]
        
        ans = 0
        for i in range(n):
            for j in range(m):
                curr = abs(grid[i][j] - midEle)
                if curr % x != 0:
                    return -1
                ans += curr // x
        return ans