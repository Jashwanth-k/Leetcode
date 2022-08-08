class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        def DFS(i):
            if i >= n:
                return 0
            if i == n-1:
                return nums[i] * d[nums[i]]
            if dp[i] != -1:
                return dp[i]
            
            inclu = nums[i] * d[nums[i]] + DFS(i+2) if nums[i+1] == nums[i]+1 else nums[i] * d[nums[i]] + DFS(i+1)
            exclu = DFS(i+1)
            dp[i] = max(inclu,exclu)
            return dp[i]
        
        d = Counter()
        for i in nums:
            d[i] += 1
        nums = sorted(d.keys())
        n = len(nums)
        dp = [-1]*n
        return DFS(0)