class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(ans,nums,k,subarr):
            if len(subarr) == k:
                ans.append(subarr)
                return
            if len(nums) == 0:
                return
            
            helper(ans,nums[1:],k,subarr + [nums[0]])
            helper(ans,nums[1:],k,subarr)
            return
        
        ans = []
        nums = [i for i in range(1,n+1)]
        helper(ans,nums,k,[])
        return ans