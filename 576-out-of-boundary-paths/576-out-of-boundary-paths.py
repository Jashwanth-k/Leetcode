class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        def DFS(m,n,i,j,maxMove,dp):
            if maxMove < 0:
                return 0
            if (i < 0 or j < 0 or i == m or j == n) and maxMove >= 0:
                return 1
            if (i,j,maxMove) in dp:
                return dp[i,j,maxMove]
        
            left = DFS(m,n,i,j-1,maxMove-1,dp)
            right = DFS(m,n,i,j+1,maxMove-1,dp)
            up = DFS(m,n,i-1,j,maxMove-1,dp)
            down = DFS(m,n,i+1,j,maxMove-1,dp)
            dp[i,j,maxMove] = (left + right + up + down) % (10**9+7)
            return dp[i,j,maxMove]
        
        dp = {}
        return DFS(m,n,startRow,startColumn,maxMove,dp)
            
            