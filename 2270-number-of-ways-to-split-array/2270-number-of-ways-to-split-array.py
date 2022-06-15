class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        tsum = sum(nums)
        left = right = ans = 0
        for i in range(len(nums)-1):
            left += nums[i]
            right = tsum - left
            if left >= right:
                ans += 1
        return ans