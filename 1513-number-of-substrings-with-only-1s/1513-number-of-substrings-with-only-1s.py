class Solution:
    def numSub(self, s: str) -> int:
        count = 0
        i = 0
        for j in range(len(s)):
            if s[j] == "0":
                ws = j-i
                count = (count + (ws)*(ws+1)//2) % (10**9 + 7)
                i = j+1
        j += 1
        count = (count + (j-i)*(j-i+1) // 2) % (10**9 + 7)
        return count