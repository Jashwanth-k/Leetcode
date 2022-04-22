class Solution:
    def minOperations(self, nums: List[int]) -> int:
        prev = 0
        ans = 0
        for i in nums:
            if i <= prev:   
                curr = prev + 1
                ans += curr - i
                prev = curr
            else:
                prev = i
        return ans