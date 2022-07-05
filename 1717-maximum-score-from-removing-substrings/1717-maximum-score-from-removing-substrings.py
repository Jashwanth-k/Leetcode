class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def helper(s1,s2):
            nonlocal s
            stack,count = [],0
            for i in s:
                if stack and stack[-1] == s1 and i == s2:
                    stack.pop()
                    count += 1
                else:
                    stack.append(i)
            s = "".join(stack)
            return count
        
        if x >= y:
            ct1 = helper("a","b") 
            ct2 = helper("b","a")
            return ct1 * x + ct2 * y
        else:
            ct1 = helper("b","a")
            ct2 = helper("a","b")
            return ct1 * y + ct2 * x