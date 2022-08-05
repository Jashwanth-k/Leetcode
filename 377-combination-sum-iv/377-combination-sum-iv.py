from bisect import bisect_left
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def DFS(target):
            if target == 0:
                return 1
            if target in dp:
                return dp[target]
            
            res = 0
            idx = bisect_left(nums,target)
            idx = idx - 1 if idx == n or nums[idx] != target else idx
            for i in range(idx+1):
                res += DFS(target - nums[i])
            dp[target] = res
            return res
        
        nums.sort()
        n = len(nums)
        dp = {}
        return DFS(target)