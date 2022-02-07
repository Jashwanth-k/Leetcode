class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] == 0: nums[i] = -1
                
        for i in range(1,n):
            nums[i] = nums[i-1] + nums[i]
            
        d = {}
        d[0] = [-1,-1]
        for i in range(n):
            if nums[i] in d:
                d[nums[i]][1] = i
            else:
                d[nums[i]] = [i,i]
        
        maxim = 0
        for i in d:
            maxim = max(maxim,d[i][1] - d[i][0])
        return maxim
