class Solution:
    def maxValue(self, n: str, x: int) -> str:
        l = len(n)
        def helper(si,ei):
            for i in range(si,ei):
                if (si == 0 and int(n[i]) < x) or (si == 1 and int(n[i]) > x):
                    return n[:i] + str(x) + n[i:]
            return n + str(x)
        
        return helper(0,l) if n[0] != "-" else helper(1,l)