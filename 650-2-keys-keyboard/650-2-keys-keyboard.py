import sys
sys.setrecursionlimit(10000)
class Solution:
    def minSteps(self, n: int) -> int:
        def stepsHelper(n, s, cop,dp):
            if len(s) == n:
                return 0
            if len(s) > n:
                return float('inf')
            if (s,cop) in dp:
                return dp[s,cop]

            copy = float('inf')
            if cop != s:
                copy = 1 + stepsHelper(n,s,s,dp)
            paste = 1 + stepsHelper(n, s + cop, cop,dp)
            dp[s,cop] = min(copy, paste)
            return dp[s,cop]
        
        if n == 1:
            return 0
        dp = {}
        return 1 + stepsHelper(n, "A", "A",dp)