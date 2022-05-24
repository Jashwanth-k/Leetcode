class Solution:    
    def countSubstrings(self, s: str) -> int:
        def helper(s,si,ei):
            count = 0
            while si >= 0 and ei < n and s[si] == s[ei]:
                si -= 1
                ei += 1
                count += 1
            return count
        
        n = len(s)
        if n == 1: return 1
        output = 1
        for i in range(n - 1):
            ans1 = helper(s, i, i)
            ans2 = helper(s, i, i + 1)
            output += ans1 + ans2
        return output