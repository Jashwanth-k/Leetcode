class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        def coinsHelper(piles, k, i, n,dp):
            if k == 0 or i >= n:
                return 0
            if dp[i][k] != -1:
                return dp[i][k]

            ans = float('-inf')
            curans = 0
            maxlen = min(k,len(piles[i]))+1
            for pick in range(maxlen):
                subans = coinsHelper(piles, k - pick, i + 1, n,dp)
                if pick-1 >= 0:
                    curans += piles[i][pick-1]
                ans = max(curans + subans, ans)
            dp[i][k] = ans
            return ans

        n = len(piles)
        dp = [[-1]*(k+1) for j in range(n)]
        return coinsHelper(piles, k, 0, n,dp)