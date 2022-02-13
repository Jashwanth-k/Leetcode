class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def find_subset(nums,idx=0,output=[[]]):
            if idx >= len(nums):
                return output

            for j in range(len(output)):
                output.append(output[j] + [nums[idx]])

            return find_subset(nums,idx+1,output)
        return find_subset(nums)