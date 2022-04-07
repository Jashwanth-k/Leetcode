class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def stoneHelper(stones,n):
            if len(stones) == 1:
                return stones[0]
            
            stones.sort()
            x,y = stones[-2],stones[-1]
            val = y - x
            return stoneHelper(stones[:-2] + [val],n)
            
        n = len(stones)
        return stoneHelper(stones,n)