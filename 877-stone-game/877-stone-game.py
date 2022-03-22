class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        def stoneHelper(piles, state, alice, bob,dp,i,j):
            if i > j:
                return alice > bob
            
            if (i,j,state) in dp:
                return dp[i,j,state]

            if state == 1:
                first = stoneHelper(piles, abs(state - 1), alice + piles[i], bob,dp,i+1,j)
                last = stoneHelper(piles, abs(state - 1), alice + piles[j], bob,dp,i,j-1)
            else:
                first = stoneHelper(piles, abs(state - 1), alice, bob + piles[i],dp,i+1,j)
                last = stoneHelper(piles, abs(state - 1), alice, bob + piles[j],dp,i,j-1)
            dp[i,j,state] = first or last
            return dp[i,j,state]
        
        n = len(piles)
        dp = {}
        return stoneHelper(piles, 1, 0, 0,dp,n-1,n-1)