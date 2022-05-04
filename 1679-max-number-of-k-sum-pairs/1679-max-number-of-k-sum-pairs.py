class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = collections.defaultdict(int)
        ans = 0
        for i in nums:
            ele = k - i
            if d[ele] != 0:
                ans += 1
                d[ele] -= 1
            else:
                d[i] += 1
        return ans
            