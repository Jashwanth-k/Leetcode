class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i,j = 0,len(piles)-1
        ans = 0
        while j-i+1 >= 3:
            ans += piles[j-1]
            i += 1
            j -= 2
        return ans