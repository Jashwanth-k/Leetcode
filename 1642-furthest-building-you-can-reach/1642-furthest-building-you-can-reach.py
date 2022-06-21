class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        i = -1
        minHeap = [0] * ladders
        totalCost = 0
        for i in range(n-1):
            currHeight = abs(heights[i]-heights[i+1]) if heights[i] < heights[i+1] else 0
            if minHeap and currHeight > minHeap[0]:
                totalCost += heapq.heapreplace(minHeap, currHeight)
            else:
                totalCost += currHeight
            if totalCost > bricks:
                return i 
        return i+1