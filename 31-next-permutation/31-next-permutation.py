class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        for i in range(n-1,-1,-1):
            cur,idx = 1e4,None
            for j in range(i+1,n):
                if nums[j] > nums[i] and nums[j] < cur:
                    cur = nums[j]
                    idx = j
                    
            if idx != None and cur > nums[i]:
                nums[i],nums[idx] = nums[idx],nums[i]
                for k in range(i+1,n):
                    mi = k
                    for l in range(k+1,n):
                        if nums[l] < nums[mi]:
                            mi = l
                    nums[k],nums[mi] = nums[mi],nums[k]
                break
        if idx == None:
            for i in range(((n-1)//2)+1):
                nums[i],nums[n-1-i] = nums[n-1-i],nums[i]
        return