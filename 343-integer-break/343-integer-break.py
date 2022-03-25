class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for i in range(n + 1)]
        dp[0] = dp[1] = 1

        ans = float('-inf')
        for i in range(2, n + 1):
            for j in range(i, 0, -1):
                if j == i: j -= 1
                pick1 = j * dp[i - j]
                pick2 = j * (i-j)
                ans = max(pick1,pick2, ans)
            dp[i] = ans
        return ans
        