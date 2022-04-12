class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        def subsetHelper(nums,i,prev,dp):
            if i < 0:
                return []
            if dp[i][prev+1] != -1:
                return dp[i][prev+1]
            
            ans1 = []
            if prev == -1 or nums[prev] % nums[i] == 0:
                ans1 = subsetHelper(nums,i-1,i,dp) + [nums[i]]
            ans2 = subsetHelper(nums,i-1,prev,dp)
            
            if len(ans1) >= len(ans2):
                dp[i][prev+1] = ans1
            else:
                dp[i][prev+1] = ans2
            return dp[i][prev+1]
        
        n = len(nums)
        dp = [[-1]*(n+1) for j in range(n)]
        return subsetHelper(nums,n-1,-1,dp)