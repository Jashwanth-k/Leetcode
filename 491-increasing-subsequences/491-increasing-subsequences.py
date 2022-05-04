class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def helper(nums,curr,i,prev):
            if i == len(nums):
                if len(curr) > 1:
                    self.output.add(tuple(curr))
                return
            
            if nums[i] >= prev:
                helper(nums,curr + [nums[i]],i+1,nums[i])
            helper(nums,curr,i+1,prev)
            
        self.output = set()
        helper(nums,[],0,float('-inf'))
        return self.output