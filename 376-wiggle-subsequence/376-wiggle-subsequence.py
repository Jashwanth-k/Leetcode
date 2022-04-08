class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0]*(2) for j in range(n)]
        
        for i in range(1,n):
            for state in range(2):
                include = 0
                if state == 0:
                    if nums[i] - nums[i-1] > 0:
                        include = 1 + dp[i-1][1]
                if state == 1:
                    if nums[i] - nums[i-1] < 0:
                        include = 1 + dp[i-1][0]        
                exclude = dp[i-1][state]
                dp[i][state] = max(include,exclude)     
                
        return 1 + max(dp[-1][0],dp[-1][1])