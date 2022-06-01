class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        maxHeap = []
        for size in range(1,n+1):
            i = 0
            currSum = 0
            for j in range(n):
                currSum += nums[j]
                if (j-i+1) == size:
                    if len(maxHeap) == right:
                        if -maxHeap[0] > currSum:
                            heapq.heapreplace(maxHeap, -currSum)
                    else:
                        heapq.heappush(maxHeap,-currSum)
                    currSum -= nums[i]
                    i += 1
        
        ans = 0
        for i in range(left-1,right):
            ans = (ans + -heapq.heappop(maxHeap)) % (10**9 + 7)
        return ans