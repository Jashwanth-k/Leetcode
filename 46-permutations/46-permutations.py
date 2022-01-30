class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(nums,i=0):
            if i == len(nums)-1:
                return [[nums[i]]]
            
            smalloutput = helper(nums,i+1)
            output = []
            for sublist in smalloutput:
                for j in range(len(sublist) + 1):
                    output.append(sublist[:j] + [nums[i]] + sublist[j:])
            return output
        return helper(nums)