class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(s,si,ei):
            while si >= 0 and ei < n and s[si] == s[ei]:
                si -= 1
                ei += 1
            return s[si+1:ei]
        
        n = len(s)
        if n == 1: return s
        output = ""
        for i in range(n - 1):
            ans1 = helper(s, i, i)
            ans2 = helper(s, i, i + 1)
            n1,m1,m2 = len(output),len(ans1),len(ans2)
            if m1 >= m2 and m1 > n1:
                output = ans1
            elif m2 > n1:
                output = ans2
        return output