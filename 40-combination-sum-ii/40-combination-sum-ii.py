class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def helper(candidates,target,res,path):
            if target == 0:
                res.append(path)
                return
            
            if target < 0 or len(candidates) == 0:
                return
            
            for i in range(len(candidates)):
                if i > 0 and candidates[i] == candidates[i-1]:
                    continue
                helper(candidates[i+1:],target - candidates[i],res,path + [candidates[i]])
        
        res = []
        helper(candidates,target,res,[])
        return res