class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        
        smalloutput = self.permuteUnique(nums[1:]) 
        output = []
        for sublist in smalloutput:
            for j in range(len(nums)):
                ans = sublist[:j] + [nums[0]] + sublist[j:]
                if ans not in output:
                    output.append(ans)
        return output