from heapq import heapify,heappop
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        req = n // 2
        bucket = [0] * (max(arr)+1)
        for i in arr:
            bucket[i] -= 1
        
        res = 0
        heapify(bucket)
        while n > req:
            n -= -heappop(bucket)
            res += 1
        return res