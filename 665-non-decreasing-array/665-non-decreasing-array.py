class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        def left_right(nums):
            flag = False
            for i in range(n-1):
                if i == 0:
                    if nums[i] > nums[i+1]:
                        nums[i] = nums[i+1]
                        flag = True
                    continue
                if nums[i] > nums[i+1]:
                    nums[i+1] = nums[i]
                    if flag: return False
                    flag = True
            return True
        
        def right_left(nums):
            flag = False
            for i in range(n-1,-1,-1):
                if i == n-1:
                    if nums[i] < nums[i-1]:
                        nums[i] = nums[i-1]
                        flag = True
                    continue
                if nums[i] > nums[i+1]:
                    nums[i] = nums[i+1]
                    if flag: return False
                    flag = True
            return True
        return left_right(nums[:]) or right_left(nums[:])
                    