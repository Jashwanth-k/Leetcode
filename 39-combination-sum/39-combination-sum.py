class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(candidates,target,res,path):
            if target == 0:
                res.append(path)
                return 
            
            if len(candidates) == 0 or target < 0:
                return
            
            helper(candidates,target-candidates[0],res,path + [candidates[0]])
            helper(candidates[1:],target,res,path)
            
        res = []
        helper(candidates,target,res,[])
        return res