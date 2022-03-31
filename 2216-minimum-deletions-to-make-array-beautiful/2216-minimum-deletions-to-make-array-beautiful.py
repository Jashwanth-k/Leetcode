class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        n = len(nums)
        delete = 0
        i = 0
        while i < n:
            if (i - delete) % 2 == 0 and i + 1 < n and nums[i] == nums[i + 1]:
                delete += 1
            i += 1
        if (n-delete) % 2 != 0:
            delete += 1
        return delete
                