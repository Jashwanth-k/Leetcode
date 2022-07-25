class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)        
        res, i, j = 0, 0, 1
        prev = None
        while j <= n:
            if j < n and (prev == None or nums[j-1] - nums[j] == prev):
                prev = nums[j-1] - nums[j]
                j += 1
            else:
                if j - i >= 3:
                    k = (j-i)-3 + 1
                    res += k*(k+1) // 2
                prev = None
                i = j - 1
                if j == n:
                    break
        return res