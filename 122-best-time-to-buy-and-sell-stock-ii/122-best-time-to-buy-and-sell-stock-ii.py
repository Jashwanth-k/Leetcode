class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def profitHelper(prices,i,hold):
            if i < 0:
                return 0
            if hold != None:
                if prices[i] < hold:
                    return hold - prices[i]
                else:
                    return 0
            
            ans1 = 0
            if hold == None:
                ans1 = profitHelper(prices,i-1,prices[i])
            ans2 = profitHelper(prices,i-1,None)
            return ans1 + ans2
        
        n = len(prices)
        return profitHelper(prices,n-1,None)