class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        i = 0
        ct = 0
        for j in range(n):
            if j > 0 and prices[j - 1] - prices[j] != 1:
                curLen = (j - i)
                ct += (curLen * (curLen + 1) // 2) - curLen
                i = j
        ct += (j-i+1)*(j-i+1+1)//2 - (j-i+1)
        return ct + n