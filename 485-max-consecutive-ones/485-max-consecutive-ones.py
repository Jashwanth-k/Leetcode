class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev = None
        ans = 0
        for curr in range(len(nums)):
            if nums[curr] == 1:
                if prev == None:
                    prev = curr
                    ans = max(ans,1)
                else:
                    ans = max(ans,curr-prev+1)
            else:
                prev = None
        return ans