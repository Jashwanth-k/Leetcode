import heapq
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(k):
            heapq.heapreplace(nums,nums[0]+1)
        curr = 1
        for i in nums:
            curr = (curr * i) % (10**9+7)
        return curr