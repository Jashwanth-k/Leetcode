class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)
        def zigzagHelper(si, helper):
            ans = 0
            for i in range(si, n, 2):
                left = helper[i - 1] if i - 1 >= 0 else -1
                right = helper[i + 1] if i + 1 < n else -1
                curr = helper[i]

                if left >= curr:
                    diff = left - curr + 1
                    ans += diff
                    helper[i-1] -= diff
                if right >= curr:
                    diff = right - curr + 1
                    ans += diff
                    helper[i+1] -= diff
            return ans

        ans1 = zigzagHelper(0, nums[:])
        ans2 = zigzagHelper(1, nums[:])
        return min(ans1, ans2)