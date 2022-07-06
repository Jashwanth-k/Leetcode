class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def DFS(r,c):
            if (r,c) in dp:
                return dp[r,c]
            paths = [[r,c+1],[r,c-1],[r+1,c],[r-1,c]]
            ans = 1
            for i,j in paths:
                if 0 <= i < m and 0 <= j < n and matrix[i][j] > matrix[r][c]:
                    curr = 1 + DFS(i,j)
                    ans = max(ans,curr)
            dp[r,c] = ans
            return dp[r,c]
        
        dp = {}
        m,n = len(matrix),len(matrix[0])
        output = 0
        for i in range(m):
            for j in range(n):
                output = max(DFS(i,j),output)
        return output