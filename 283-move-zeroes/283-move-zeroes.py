class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        nums.append(0)
        prev = nums.index(0)
        for i in range(prev+1,n):
            if nums[i] != 0:
                nums[prev] = nums[i]
                nums[i] = 0
                prev += 1
        nums.pop()
        return
            