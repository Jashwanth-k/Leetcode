class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        maxNbr = nums[0]
        for i in range(1,len(nums)):
            maxNbr = max(maxNbr + 1,nums[i])
            if nums[i] <= maxNbr:
                res += maxNbr - nums[i]
        return res