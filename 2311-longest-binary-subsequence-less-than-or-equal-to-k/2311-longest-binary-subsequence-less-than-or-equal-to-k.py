class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        substr = ""
        for i in range(len(s)-1,-1,-1):
            substr = s[i] + substr
            if int(substr,2) > k:
                return s[:i].count("0") + len(substr)-1
        return len(s)