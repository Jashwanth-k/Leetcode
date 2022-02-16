import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = j = 0
        maxHeap = []
        output = []
        while j < len(nums):
            heapq.heappush(maxHeap,[-nums[j],j])
            if (j-i+1) == k:
                while maxHeap[0][1] < i or maxHeap[0][1] > j:
                    heapq.heappop(maxHeap)
                
                output.append(-maxHeap[0][0])
                if nums[i] == -maxHeap[0][0]:
                    heapq.heappop(maxHeap)
                i += 1
                j += 1
            else:
                j += 1
        return output