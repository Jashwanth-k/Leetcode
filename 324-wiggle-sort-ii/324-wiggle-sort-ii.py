class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        end = max(nums)
        bucket = [0]*(end+1)
        for i in nums:
            bucket[i] += 1
        order = [i for i in range(end+1) if bucket[i] != 0]
        
        def helper(st):
            for i in range(st,n,2):
                ele = order[-1]
                nums[i] = ele
                bucket[ele] -= 1
                if bucket[ele] == 0:
                    order.pop()
        helper(1)
        helper(0)