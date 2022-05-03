class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        tsum = sum(nums)
        k = tsum - x
        n = len(nums)
        if k == 0:
            return n
        i,j = 0,0
        currSum = 0
        size = 0
        while j < n:
            currSum += nums[j]
            if currSum > k:
                while currSum > k and i < n:
                    currSum -= nums[i]
                    i += 1
                    
            if currSum == k:
                size = max(j-i+1,size)
            j += 1
        
        return n - size if size != 0 else -1