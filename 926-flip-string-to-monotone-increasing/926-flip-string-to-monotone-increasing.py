class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        if n == 1: return 0
        ans1,ans2 = s.count("0"),s.count("1")
        suffix = [0]*n
        z = 0
        for i in range(n-1,-1,-1):
            if s[i] == "0":
                z += 1
            suffix[i] = z
       
        ans3 = 1e10
        prefix = 0
        for i in range(n-1):
            if s[i] == "1":
                prefix += 1
            ans3 = min(ans3,prefix + suffix[i+1])
        return min(ans1,ans2,ans3)