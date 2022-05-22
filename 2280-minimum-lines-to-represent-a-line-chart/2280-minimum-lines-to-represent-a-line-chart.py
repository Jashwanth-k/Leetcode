from fractions import Fraction
class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:            
        n = len(stockPrices)
        if n == 1: return 0
        stockPrices.sort(key=lambda x: x[0])
        ans = 0
        prev = None
        for i in range(n-1):
            curr,nxt = stockPrices[i],stockPrices[i+1]
            if prev == None:
                prev = Fraction(nxt[1] - curr[1]) / (nxt[0] - curr[0])
                continue
            
            nextChange = Fraction(nxt[1] - curr[1]) / (nxt[0] - curr[0])
            if prev == nextChange:
                continue
            else:
                prev = nextChange
                ans += 1
        return ans+1
                
            
            