class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def uniquePathsHelper(m,n,i,j,dp):
            if i == m-1 and j == n-1:
                return 1
            
            if i >= m or j >= n:
                return 0
            
            if dp[i][j] != -1: return dp[i][j]
            
            right = uniquePathsHelper(m,n,i,j+1,dp)
            down = uniquePathsHelper(m,n,i+1,j,dp)
            dp[i][j] = right+down
            return dp[i][j]
        
        dp = [[-1]*n for i in range(m)]
        return uniquePathsHelper(m,n,0,0,dp)
    