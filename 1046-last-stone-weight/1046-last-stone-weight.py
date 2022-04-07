import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones)
        while len(stones) > 1:
            y = heapq._heappop_max(stones)
            x = heapq._heappop_max(stones)
            val = y-x
            stones.append(val)
            heapq._siftdown_max(stones,0,len(stones)-1)
        return stones[0]