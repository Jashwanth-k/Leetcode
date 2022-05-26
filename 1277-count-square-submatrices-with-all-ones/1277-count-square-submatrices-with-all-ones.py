class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[0]*(m) for j in range(n)]
        count = 0
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if matrix[i][j] == 0:
                    continue
                count += 1
                path = [[i+1,j],[i,j+1],[i+1,j+1]]
                if all(0 <= r < n and 0 <= c < m and matrix[r][c] == 1 for r,c in path):
                    dp[i][j] = 1 + min(dp[i+1][j+1],dp[i+1][j],dp[i][j+1])
                    count += dp[i][j]
        return count