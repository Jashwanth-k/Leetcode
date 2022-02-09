class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPurchase = prices[0]
        for n in prices:
            maxProfit = max(maxProfit,n - minPurchase)
            minPurchase = min(minPurchase,n)
        return maxProfit
    