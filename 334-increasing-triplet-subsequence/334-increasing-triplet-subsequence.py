class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3: return False
        suffix = [0]*(n+1)
        for i in range(n-1,-1,-1):
            suffix[i] = max(nums[i],suffix[i+1])
        
        prefix = nums[0]
        for i in range(1,n-1):
            if prefix < nums[i] < suffix[i+1]:
                return True
            prefix = min(prefix,nums[i])
        return False