class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def partitionHelper(nums,k,i):
            if k == 0:
                return True
            
            if k < 0 or i < 0:
                return False
            
            if dp[i][k] != -1: return dp[i][k]
            
            inclu = partitionHelper(nums,k-nums[i],i-1)
            exclu = partitionHelper(nums,k,i-1)
            dp[i][k] = inclu or exclu
            return dp[i][k]
        
        n,s = len(nums),sum(nums)
        if s % 2 != 0:
            return False
        k = s // 2
        dp = [[-1]*(k+1) for j in range(n)]
        return partitionHelper(nums,k,n-1)