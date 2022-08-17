class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        helper = sorted(nums)
        n = len(nums)
        lo,hi = (n-1)//2,-1
        for i in range(n):
            if i % 2 == 0:
                nums[i] = helper[lo]
                lo -= 1
            else:
                nums[i] = helper[hi]
                hi -= 1