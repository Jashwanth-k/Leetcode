class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        maxLen = 0
        start = 0
        d = {}
        for i in nums:
            d[i] = True
            
        for i in nums:
            subLen = 1
            if d[i] == True:
                left = i-1
                right = i+1
                
                while right in d and d[right] == True:
                    subLen += 1
                    d[right] = False
                    right += 1
                
                while left in d and d[left] == True:
                    subLen += 1
                    d[left] = False
                    left -= 1
            
            maxLen = max(subLen,maxLen)
        return maxLen
                
                