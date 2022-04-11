class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[1]*(m) for j in range(n)]
        dp[0][0] = [grid[0][0],grid[0][0]]

        for i in range(n):
            for j in range(m):
                curr = grid[i][j]
                if i == 0 and j == 0:
                    continue

                left = right = []
                if j - 1 >= 0:
                    left = dp[i][j - 1]
                if i - 1 >= 0:
                    right = dp[i - 1][j]
                total = left + right
                maxim = float('-inf')
                minim = float('inf')
                for k in total:
                    maxim = max(maxim,curr * k)
                    minim = min(minim,curr * k)
                dp[i][j] = [maxim, minim]
                
        ans = max(dp[n-1][m-1])
        return -1 if ans < 0 else ans % (10**9+7)