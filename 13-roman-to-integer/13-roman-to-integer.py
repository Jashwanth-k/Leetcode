class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I" :  1,
            "V" :  5,
            "X" :  10,
            "L" :  50,
            "C" :  100,
            "D" :  500,
            "M" :  1000
        }
        count = 0
        prev = 0
        for i in range(len(s)-1,-1,-1):
            ans = d[s[i]]
            if ans >= prev:
                count += ans
            else:
                count -= ans
            prev = ans
        return count
                