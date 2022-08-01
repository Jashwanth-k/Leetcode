class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        mod = 10**9 + 7
        imp = [0]*(n+1)
        for i,j in requests:
            imp[i] += 1
            imp[j+1] -= 1
        for i in range(1,n):
            imp[i] += imp[i-1]
        
        nums.sort(reverse=True)
        imp.sort(reverse=True)
        res = 0
        for i in range(n):
            res = (res + (nums[i] * imp[i]) % mod) % mod
        return res