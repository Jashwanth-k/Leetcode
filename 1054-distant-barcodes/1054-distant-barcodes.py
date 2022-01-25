import heapq
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        heap = []
        d = {}
        for i in barcodes:
            d[i] = d.get(i,0) + 1
            
        for i in d:
            heap.append([d[i],i])
        heapq._heapify_max(heap)
        
        n = len(barcodes)
        output = [0] * n
        i = 0
        while i < n:
            output[i] = heap[0][1]
            heap[0][0] -= 1
            if heap[0][0] == 0:
                heapq._heappop_max(heap)
            i += 2
            
        i = 1
        while i < n:
            output[i] = heap[0][1]
            heap[0][0] -= 1
            if heap[0][0] == 0:
                heapq._heappop_max(heap)
            i += 2
        return output
        