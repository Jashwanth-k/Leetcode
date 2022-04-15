class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n,m = len(dungeon),len(dungeon[0])
        dp = [[float('inf')]*(m+1) for j in range(n+1)]
        last = dungeon[-1][-1]
        dp[n-1][m-1] = 1+(-last) if last < 0 else 1
        
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if i == n-1 and j == m-1:
                    continue
                right = dp[i][j+1]
                down = dp[i+1][j]
                ans = min(right,down) - dungeon[i][j]
                dp[i][j] = 1 if ans <= 0 else ans
        return dp[0][0]
                