class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def DFS(nums,result,path):
            if len(nums) == 0:
                result.append(path)
                return
            
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                
                DFS(nums[:i] + nums[i+1:],result,path + [nums[i]])
                
        result = []
        DFS(nums,result,[])
        return result
    