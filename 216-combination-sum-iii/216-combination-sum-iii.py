class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def helper(nums,i,k,n,path):
            if n == 0 and k == 0:
                self.ans.append(path)
                return 
            if k == 0 or i < 0:
                return
            helper(nums,i-1,k-1,n-nums[i],path+[nums[i]])
            helper(nums,i-1,k,n,path)
                
        self.ans = []
        nums = [i for i in range(1,10)]
        helper(nums,8,k,n,[])
        return self.ans