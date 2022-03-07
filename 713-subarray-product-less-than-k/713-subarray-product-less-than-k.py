class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        i = j = 0
        currPro = 1
        output = 0
        while j < len(nums):
            currPro *= nums[j]
            if currPro >= k:
                while currPro >= k and i <= j:
                    currPro //= nums[i]
                    i += 1
            if currPro < k:
                output += j-i+1
            j += 1
        return output