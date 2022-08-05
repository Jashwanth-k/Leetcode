class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        dp = [0]*(target+1)
        dp[0] = 1
        for tar in range(1,target+1):
            res = 0
            for i in range(n):
                if nums[i] > tar: break 
                res += dp[tar - nums[i]]
            dp[tar] = res
        return dp[-1]