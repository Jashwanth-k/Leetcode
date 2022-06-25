class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        def checkArr(arr):
            for i in range(n-1):
                if arr[i] > arr[i+1]:
                    return False
            return True
        
        n = len(nums)
        left = nums[:]
        right = nums[:]
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                left[i] = nums[i+1]
                right[i+1] = nums[i]
                return checkArr(left) or checkArr(right)
        return True