class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        totalneg = 0
        for k in nums:
            if k < 0: totalneg += 1
        maxLen = 0
        currMinus = 0

        for j in range(n):
            if nums[j] < 0:
                totalneg -= 1
                currMinus += 1
            while (nums[j] == 0 and currMinus % 2 != 0) or (currMinus % 2 != 0 and totalneg == 0):
                if nums[i] < 0:
                    currMinus -= 1
                i += 1
            if currMinus % 2 == 0:
                maxLen = max(maxLen, j - i + 1) if nums[j] != 0 else max(maxLen, j - i)
            if nums[j] == 0:
                i = j + 1
        return maxLen