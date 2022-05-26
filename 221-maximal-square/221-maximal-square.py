class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n,m = len(matrix),len(matrix[0])
        dp = [[0]*(m) for j in range(n)]
        ans = 0
        check = False
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if matrix[i][j] == "0":
                    continue
                ans = max(ans,1)
                paths = [[i+1,j],[i,j+1],[i+1,j+1]]
                if all(0 <= r < n and 0 <= c < m and matrix[r][c] == "1" for r,c in paths):
                    dp[i][j] = 1 + min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1])
                    ans = max(ans,dp[i][j])
                    check = True
                    
        if check:
            return (ans+1)*(ans+1)
        return ans*ans