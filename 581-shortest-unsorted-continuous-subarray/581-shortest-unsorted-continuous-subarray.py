class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        helper = nums[:]
        helper.sort()
        left = 0
        right = -1
        for i in range(len(nums)-1):
            if helper[i] != nums[i]:
                left = i
                break
            
        for i in range(len(nums)-1,0,-1):
            if helper[i] != nums[i]:
                right = i
                break
        return right - left + 1