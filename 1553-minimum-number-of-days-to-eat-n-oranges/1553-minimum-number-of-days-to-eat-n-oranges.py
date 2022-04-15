class Solution:
    def minDays(self, n: int) -> int:
        def daysHelper(n,dp):
            if n <= 1:
                return n
            if n in dp:
                return dp[n]
        
            ans1 = n%2 + daysHelper(n//2,dp)
            ans2 = n%3 + daysHelper(n//3,dp)
                
            dp[n] = 1 + min(ans1,ans2)
            return dp[n]
        
        dp = {}
        return daysHelper(n,dp)