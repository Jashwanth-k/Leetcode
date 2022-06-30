class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mid = len(nums) // 2
        val = nums[mid]
        totalMoves = 0
        for i in nums:
            totalMoves += abs(i-val)
        return totalMoves