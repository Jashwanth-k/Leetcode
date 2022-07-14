from heapq import heappush,heappop,heapify
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        pq = []
        mid = n-k+1
        for i in range(mid):
            pq.append([nums[i],i])
        heapify(pq)
        
        res,idx = [],-1
        while len(res) != k:
            while pq and pq[0][1] < idx:
                heappop(pq)
            curr,idx = heappop(pq)
            res.append(curr)
            if mid < n:
                heappush(pq,[nums[mid],mid])
            mid += 1
        return res