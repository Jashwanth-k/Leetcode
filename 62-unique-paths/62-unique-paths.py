class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def uniquePathsHelper(i, j, m, n, grid):
            if i == m - 1 and j == n - 1:
                return 1

            if i >= m or j >= n:
                return 0

            ans1 = ans2 = 0
            if grid[i][j+1] == 0:
                ans1 = uniquePathsHelper(i, j + 1, m, n, grid)
            else:
                ans1 = grid[i][j+1]
            if grid[i+1][j] == 0:
                ans2 = uniquePathsHelper(i + 1, j, m, n, grid)
            else:
                ans2 = grid[i+1][j]
            grid[i][j] = ans1 + ans2
            return ans1 + ans2

        grid = [[0 for i in range(m+100)] for j in range(n+100)]
        return uniquePathsHelper(0, 0, m, n, grid)
        