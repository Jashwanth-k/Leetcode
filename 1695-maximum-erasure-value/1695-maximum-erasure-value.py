class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        i = 0
        d = {}
        currSum = ans = 0
        for j in range(len(nums)):
            currSum += nums[j]
            d[nums[j]] = d.get(nums[j],0) + 1
            while len(d) != j-i+1:
                currSum -= nums[i]
                d[nums[i]] -= 1
                if d[nums[i]] == 0:
                    d.pop(nums[i])
                i += 1
            ans = max(ans,currSum)
        return ans