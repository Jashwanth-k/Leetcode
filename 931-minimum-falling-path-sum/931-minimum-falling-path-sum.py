class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1:
            return min(matrix[0])

        dp = [[float('inf')] * (n + 1) for j in range(n + 1)]
        dp[-2] = matrix[-1]
        dp[-2].append(float('inf'))

        ans = float('inf')
        for i in range(n - 2, -1, -1):
            for j in range(n - 1, -1, -1):
                curr = min(dp[i + 1][j], dp[i + 1][j + 1], dp[i + 1][j - 1])
                dp[i][j] = matrix[i][j] + curr
                if i == 0:
                    ans = min(ans, dp[i][j])
        return ans
                    