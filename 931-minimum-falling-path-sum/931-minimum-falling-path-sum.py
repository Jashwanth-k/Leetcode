class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def fallingHelper(matrix,n,i,j,dp):
            if j < 0 or j >= n or i < 0:
                return float('inf')
            
            if i == 0:
                return matrix[i][j]
            
            if dp[i][j] != -1 : return dp[i][j]
            
            rightdia = fallingHelper(matrix,n,i-1,j+1,dp)
            up = fallingHelper(matrix,n,i-1,j,dp)
            leftdia = fallingHelper(matrix,n,i-1,j-1,dp)
            dp[i][j] = matrix[i][j] + min(leftdia,up,rightdia)
            return dp[i][j]
        
        n = len(matrix)
        dp = [[-1]*n for j in range(n)]
        ans = float('inf')
        for k in range(n):
            currans = fallingHelper(matrix,n,n-1,k,dp)
            ans = min(currans,ans)
        return ans