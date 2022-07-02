class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        maxVal = [float("-inf")]*n
        minVal = [float("inf")]*n
        maxVal[0],minVal[-1] = nums[0],nums[-1]
        for i in range(1,n):
            maxVal[i] = max(maxVal[i-1],nums[i])
        for i in range(n-2,-1,-1):
            minVal[i] = min(minVal[i+1],nums[i])
        
        ans = 0
        for i in range(1,n-1):
            if maxVal[i-1] < nums[i] and nums[i] < minVal[i+1]:
                ans += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                ans += 1
        return ans