class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        def calcHelper(dungeon,i,j,n,m,dp):
            if i == n-1 and j == m-1:
                if dungeon[i][j] < 0:
                    return 1 + -dungeon[i][j]
                return 1
            if i >= n or j >= m:
                return float('inf')
            
            if dp[i][j] != float('inf'):
                return dp[i][j]
            
            right = calcHelper(dungeon,i,j+1,n,m,dp)
            down = calcHelper(dungeon,i+1,j,n,m,dp)
            
            ans = min(right,down) - dungeon[i][j]
            if ans <= 0:
                dp[i][j] = 1
            else:
                dp[i][j] = ans
            return dp[i][j]
        
        n,m = len(dungeon),len(dungeon[0])
        dp = [[float('inf')]*(m) for j in range(n)]
        return calcHelper(dungeon,0,0,n,m,dp)
    