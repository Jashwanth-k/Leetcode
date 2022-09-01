class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        def reverse(si,ei):
            while si <= ei:
                nums[si],nums[ei] = nums[ei],nums[si]
                si += 1
                ei -= 1
                
        n = len(nums)
        flag = True
        for i in range(n-1,0,-1):
            if nums[i-1] < nums[i]:
                flag = False
                cur,idx = 1e4,None
                for j in range(i,n):
                    if nums[j] > nums[i-1] and nums[j] <= cur:
                        cur = nums[j]
                        idx = j
                nums[i-1],nums[idx] = nums[idx],nums[i-1]
                reverse(i,n-1)
                break
        if flag:
            reverse(0,n-1)
        return