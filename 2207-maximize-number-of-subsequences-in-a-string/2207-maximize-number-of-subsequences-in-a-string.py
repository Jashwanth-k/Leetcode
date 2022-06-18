class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        start = end = prefix = sub = 0
        for i in text:
            if i == pattern[1]:
                prefix += 1
                end += 1
            elif i == pattern[0]:
                start += 1
                sub += prefix
        if pattern[0] == pattern[1]: return end * (end + 1) // 2
        return max((start+1)*end - sub,start*(end+1) - sub)