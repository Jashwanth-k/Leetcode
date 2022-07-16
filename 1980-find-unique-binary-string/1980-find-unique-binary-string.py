class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums = set(nums)
        for s in nums:
            for i in range(len(s)):
                zero = s[:i] + "0" + s[i+1:]
                if zero not in nums:
                    return zero
                one = s[:i] + "1" + s[i+1:]
                if one not in nums:
                    return one
        return