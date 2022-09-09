class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        i = prev = 0
        while i < n and prev < n:
            while prev < n and nums[prev] != 0:
                prev += 1
            if nums[i] != 0:
                i += 1
                continue
            for j in range(i + 1, n):
                if nums[j] != 0:
                    nums[prev], nums[j] = nums[j], nums[prev]
                    i = j
                    break
            else:
                i += 1
        return nums