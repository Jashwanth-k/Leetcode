class Solution:
    def jump(self, nums: List[int]) -> int:
        def jumpHelper(nums,i,n,dp):
            if i == n-1:
                return 0
            if nums[i] == 0:
                return float('inf')
            
            if dp[i] != -1:
                return dp[i]
            
            ans = float('inf')
            limit = min(nums[i],n-i-1)
            for jump in range(1,limit+1):
                currans = 1 + jumpHelper(nums,i+jump,n,dp)
                ans = min(currans,ans)
            dp[i] = ans
            return dp[i]
        
        n = len(nums)
        dp = [-1]*(n)
        return jumpHelper(nums,0,n,dp)