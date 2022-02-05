class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i for i in range(1,10)]
        def helper(nums,k,n,res,path):
            if n == 0:
                if len(path) == k:
                    res.append(path)
                return
            
            if n < 0 or len(nums) == 0 or len(path) > k:
                return
            
            helper(nums[1:],k,n - nums[0],res,path + [nums[0]])
            helper(nums[1:],k,n,res,path)
            
        res = []
        helper(nums,k,n,res,[])
        return res