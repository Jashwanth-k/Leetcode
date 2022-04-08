class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        def wiggleHelper(nums,i,state,dp):
            if i == 0:
                return 0
            if dp[i][state] != -1:
                return dp[i][state]
            
            include = 0
            if state == 0:
                if nums[i] - nums[i-1] > 0:
                    include = 1 + wiggleHelper(nums,i-1,1,dp)
            if state == 1:
                if nums[i] - nums[i-1] < 0:
                    include = 1 + wiggleHelper(nums,i-1,0,dp)
            exclude = wiggleHelper(nums,i-1,state,dp)
            dp[i][state] = max(include,exclude)        
            return dp[i][state]
                    
        n = len(nums)
        if n == 1: return n
        if nums[-1] - nums[-2] > 0:  state = 0
        else:  state = 1
        dp = [[-1]*(2) for j in range(n)]
        return 1 + wiggleHelper(nums, n - 1, state,dp)