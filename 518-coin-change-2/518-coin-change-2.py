class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def changeHelper(coins,amount,dp,i):
            if amount == 0:
                return 1
            
            if amount < 0 or i < 0:
                return 0
            
            if dp[i][amount] != -1: return dp[i][amount]
            
            inclu = changeHelper(coins,amount-coins[i],dp,i)
            exclu = changeHelper(coins,amount,dp,i-1)
            dp[i][amount] = inclu + exclu
            return dp[i][amount]
        
        n = len(coins)
        dp = [[-1]*(amount+1) for j in range(n)]
        return changeHelper(coins,amount,dp,n-1)