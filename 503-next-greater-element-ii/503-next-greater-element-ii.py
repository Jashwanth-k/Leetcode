class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [-1]*n
        for i in range(n):
            j = (i + 1) % n
            while j != i:
                if nums[j] > nums[i]:
                    output[i] = nums[j]
                    break
                j = (j + 1) % n

        return output