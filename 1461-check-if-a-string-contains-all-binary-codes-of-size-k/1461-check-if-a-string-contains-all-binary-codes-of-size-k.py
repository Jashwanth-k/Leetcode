class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        i = 0
        uniqueEle = set()
        for j in range(len(s)):
            if (j-i+1) == k:
                uniqueEle.add(s[i:j+1])
                i += 1
        return 2**k == len(uniqueEle)