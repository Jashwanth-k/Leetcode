class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        
        res, i, j = 0, 0, 1
        prev = None
        while j <= n:
            if j < n and (prev == None or nums[j-1] - nums[j] == prev):
                prev = nums[j-1] - nums[j]
                j += 1
            else:
                if j - i >= 3:
                    for k in range(3,j-i+1):
                        res += (j - i) - k + 1
                prev = None
                i = j - 1
                if j == n:
                    break
        return res