class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        d = collections.defaultdict(int)
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                a,b = nums[i],nums[j]
                ans += d[a*b] * 8
                d[a*b] += 1
        return ans