class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s,n = sum(nums),len(nums)
        if s % 2 != 0:
            return False
        k = s // 2
        
        dp = [[0]*(k+1) for j in range(n)]
        for i in range(n): dp[i][0] = True
        for j in range(1,k+1) : dp[0][j] = False
        
        for idx in range(1,n):
            for target in range(1,k+1):
                inclu = False
                if target >= nums[idx] : inclu = dp[idx-1][target-nums[idx]]
                exclu = dp[idx-1][target]
                dp[idx][target] = inclu or exclu
        return dp[-1][-1]