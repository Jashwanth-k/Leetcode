class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        maxim = float("-inf")
        minim = float("inf")
        maxidx = minidx = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > maxim:
                maxim = nums[i]
                maxidx = i
            if nums[i] < minim:
                minim = nums[i]
                minidx = i
        li,ri = sorted([maxidx,minidx])
        left = li - 0 + 1
        right = n - ri 
        mid = ri - li
        return min(left + right,left + mid,right + mid)