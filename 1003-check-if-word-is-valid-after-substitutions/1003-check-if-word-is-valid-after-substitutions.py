class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            stack.append(i)
            if len(stack) >= 3 and stack[-1] == "c" and stack[-2] == "b" and stack[-3] == "a":
                for _ in range(3):
                    stack.pop()
        return len(stack) == 0