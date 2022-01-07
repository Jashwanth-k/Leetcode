class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums.sort()
        maxLen = 0
        i = 0
        count = 0
        while i + 1 < len(nums):
            if nums[i+1] - nums[i] == 1:
                count += 1
            elif nums[i+1] - nums[i] == 0:
                pass
            else:
                maxLen = max(maxLen,count+1)
                count = 0
            i += 1
            
        return max(maxLen,count+1)
                