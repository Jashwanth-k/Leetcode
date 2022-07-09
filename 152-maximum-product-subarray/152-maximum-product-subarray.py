class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        tNeg = sum([1 if i < 0 else 0 for i in nums])
        i = currNeg = 0
        currProd, ans = 1, 0
        for j in range(len(nums)):
            if nums[j] < 0:
                currNeg += 1
                tNeg -= 1
            if nums[j] != 0: currProd *= nums[j]
            while i <= j and (nums[j] == 0 or (currNeg % 2 != 0 and tNeg == 0)):
                if nums[i] != 0:
                    currProd //= nums[i]
                if nums[i] < 0:
                    currNeg -= 1
                i += 1
                if (j - i + 1) > 1:
                    ans = max(ans, currProd)
            if (j - i + 1) >= 1:
                ans = max(ans, currProd)
        return ans