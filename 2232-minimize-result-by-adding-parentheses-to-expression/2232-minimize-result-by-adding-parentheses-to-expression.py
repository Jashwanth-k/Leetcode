class Solution:
    def minimizeResult(self, expression: str) -> str:
        n = len(expression)
        mid = expression.index("+")
        ans = eval(expression)
        exp = "(" + expression + ")"
        for i in range(mid):
            for j in range(mid + 1, n):
                substr = expression[i:j + 1]
                remleft = expression[:i]
                remright = expression[j + 1:]
                currans = eval(substr)
                currans *= int(remleft) if remleft != "" else 1
                currans *= int(remright) if remright != "" else 1

                if currans < ans:
                    ans = currans
                    exp = remleft + "(" + substr + ")" + remright
        return exp