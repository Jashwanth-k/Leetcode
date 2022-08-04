class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        d = defaultdict(int)
        res = 0
        for i in nums:
            r = i - int(str(i)[::-1])
            res += d[r]
            d[r] += 1
        return res % (10**9 + 7)