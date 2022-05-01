class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        tsum = sum(nums)
        n = len(nums)
        ans = float('inf')
        idx = 0
        lsum = 0
        for i in range(n):
            lsum += nums[i]
            left = lsum
            right = tsum - left
            left = left // (i + 1)
            if right != 0: right = right // (n - i - 1)
            if abs(left - right) < ans:
                ans = abs(left - right)
                idx = i
        return idx