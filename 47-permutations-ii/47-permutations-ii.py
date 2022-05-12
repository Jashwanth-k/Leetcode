class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def DFS(nums,path):
            if len(nums) == 0:
                self.ans.append(path)
                return
            
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                DFS(nums[:i] + nums[i+1:],path + [nums[i]])
        self.ans = []
        DFS(nums,[])
        return self.ans