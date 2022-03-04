class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = j = 0
        minLen = float('inf')
        currSum = 0
        while j < len(nums):
            currSum += nums[j]
            if currSum >= target:
                while currSum >= target and i <= j:
                    if currSum >= target:
                        minLen = min(minLen, j - i + 1)
                    currSum -= nums[i]
                    i += 1
            j += 1
        return minLen if minLen != float('inf') else 0