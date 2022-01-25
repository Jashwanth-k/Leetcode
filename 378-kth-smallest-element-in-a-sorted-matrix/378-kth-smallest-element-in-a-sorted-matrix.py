class Solution:
    def createHeap(self,matrix,n,ct):
        heap = []
        r, c = 0, 0
        for i in range(n):
            for j in range(n):
                ct -= 1
                heap.append(matrix[i][j])
                if ct == 0:
                    r, c = i, j
                    return heap,r,c+1
                
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap,r,c = self.createHeap(matrix,n,k)

        heapq._heapify_max(heap)
        for i in range(r,n):
            for j in range(c,n):
                if matrix[i][j] < heap[0]:
                    heapq._heapreplace_max(heap,matrix[i][j])
            c = 0
        return heap[0]