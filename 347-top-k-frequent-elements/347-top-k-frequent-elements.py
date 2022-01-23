import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1

        heap = []
        for i in d:
            heap.append((d[i],i))
            heapq._siftdown_max(heap,0,len(heap)-1)

        output = []
        for _ in range(k):
            popped = heapq._heappop_max(heap)
            output.append(popped[1])
        return output