class Solution:
    def integerBreak(self, n: int) -> int:
        def breakHelper(n,st = 0):
            if n == 0:
                return 1
            
            if dp[n] != -1: return dp[n]

            ans = float('-inf')
            m = n
            if st == 0: m = n-1
            for i in range(m, 0, -1):
                pick = i * breakHelper(n - i,1)
                ans = max(pick,ans)
            dp[n] = ans
            return ans
        
        dp = [-1 for i in range(n+1)]
        return breakHelper(n)