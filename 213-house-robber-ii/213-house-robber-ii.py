class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def robber(nums):
            n = len(nums)
            prev = nums[0]
            prev2 = 0
            for i in range(2,n+1):
                curr = max(prev2 + nums[i-1],prev)
                prev2 = prev
                prev = curr
            return prev

        ans1 = robber(nums[:-1])
        ans2 = robber(nums[1:])
        return max(ans1,ans2)
