class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = 0
        maxLen = 0
        fMap = {}
        while j < len(s):
            fMap[s[j]] = fMap.get(s[j],0) + 1
            if len(fMap) < j-i+1:
                while len(fMap) < j-i+1:
                    fMap[s[i]] -= 1
                    if fMap[s[i]] == 0:
                        fMap.pop(s[i])
                    i += 1

            if len(fMap) == j-i+1:
                maxLen = max(maxLen,j-i+1)
            j += 1
        return maxLen