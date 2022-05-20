class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def helper(a,b,exp):
            if exp == "*":
                return a*b
            if exp == "+":
                return a+b
            if exp == "-":
                return a-b

        def DFS(expression, i, j):
            if expression[i:j+1].isdigit():
                return [int(expression[i:j+1])]

            output = []
            for k in range(i, j):
                if expression[k] in "+*-":
                    for l in DFS(expression, i, k - 1):
                        for m in DFS(expression, k + 1, j):
                            output.append(helper(l,m,expression[k]))
            return output
                
        n = len(expression)
        return DFS(expression,0,n-1)