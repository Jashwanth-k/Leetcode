class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part,m = list(part),len(part)
        for i in s:
            stack.append(i)
            if len(stack) >= m and stack[-m:] == part:
                stack = stack[:-m]
        return "".join(stack)