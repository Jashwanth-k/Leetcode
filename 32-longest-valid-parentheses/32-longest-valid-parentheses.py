class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        n = len(s)
        for i in range(n):
            if s[i] == ")" and stack and stack[-1][0] == "(":
                stack.pop()
            else:
                stack.append([s[i],i])
        
        if not stack: return n
        ans = 0
        ans = max(ans,stack[0][1] - 0)
        ans = max(ans,n-1-stack[-1][1])
        for i in range(len(stack)-1):
            ans = max(ans,stack[i+1][1] - stack[i][1] - 1)
        return ans