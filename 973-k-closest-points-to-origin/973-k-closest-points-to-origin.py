import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
            
        heap = []
        for i in points:
            ans = (i[0])**2 + (i[1])**2
            heap.append((ans**0.5,i))
        heapq.heapify(heap)
            
        output = []
        for _ in range(k):
            popped = heapq.heappop(heap)
            output.append(popped[1])
        return output