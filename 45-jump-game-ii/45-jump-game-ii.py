class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        
        for i in range(n-2,-1,-1):
            ans = float('inf')
            for jump in range(1,min(nums[i],n-i-1)+1):
                curans = 1 + dp[i + jump]
                ans = min(curans,ans)
            dp[i] = ans
        return dp[0]