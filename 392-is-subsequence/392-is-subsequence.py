class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        def Helper(s, t, i, j):
            if i < 0 or j < 0:
                return 0

            if s[i] == t[j]:
                ans = 1 + Helper(s, t, i - 1, j - 1)
            else:
                ans = Helper(s, t, i, j-1)
            return ans
        
        n, m = len(s), len(t)
        return Helper(s, t, n - 1, m - 1) == n