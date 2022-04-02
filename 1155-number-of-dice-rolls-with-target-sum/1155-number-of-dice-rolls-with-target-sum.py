class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        def diceRoll(i,k,target,dp):
            if target == 0 and i == 0:
                return 1
            if i == 0:
                return 0
            if dp[i][target] != -1:
                return dp[i][target]
            
            ans = 0
            for roll in range(1,k+1):
                if roll > target:
                    break
                subans = diceRoll(i-1,k,target-roll,dp)
                ans = (ans + subans) % (10**9 + 7)
            dp[i][target] = ans 
            return ans
        
        dp = [[-1]*(target+1) for j in range(n+1)]
        return diceRoll(n,k,target,dp)