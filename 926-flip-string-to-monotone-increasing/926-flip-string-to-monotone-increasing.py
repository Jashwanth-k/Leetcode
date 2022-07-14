class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        if n == 1: return 0
        ans1 = s.count("0")
        ans2 = s.count("1")
        prefix = [0]*n
        suffix = [0]*n
        
        z = o = 0
        for i in range(n):
            if s[i] == "0":
                z += 1
            prefix[i] = z
        for i in range(n-1,-1,-1):
            if s[i] == "1":
                o += 1
            suffix[i] = o
       
        ans3 = 1e10
        for i in range(n-1):
            cur1 = ((i+1) - prefix[i]) + ((n-1-i) - suffix[i+1])
            ans3 = min(ans3,cur1)
        return min(ans1,ans2,ans3)