class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        d = {}
        n = len(nums)
        for i in range(n*2):
            i = i%n
            while stack and stack[-1][1] < nums[i]:
                idx = stack.pop()[0]
                d[idx] = nums[i]
            stack.append([i,nums[i]])
        
        output = [0]*n
        for i in range(n):
            output[i] = d.get(i,-1)
        return output