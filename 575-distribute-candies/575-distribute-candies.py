class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        d = {}
        for i in candyType:
            d[i] = d.get(i,0) + 1
        
        return min(len(candyType)//2,len(d))