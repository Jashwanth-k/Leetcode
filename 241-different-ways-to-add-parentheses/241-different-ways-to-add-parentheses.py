class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def DFS(expression,i,j):
            if i == j:
                return [int(expression[i])]

            output = []
            for k in range(i, j):
                if expression[k] == "*":
                    for l in DFS(expression, i, k - 1):
                        for m in DFS(expression, k + 1, j):
                            output.append(l*m)
                elif expression[k] == "-":
                    for l in DFS(expression, i, k - 1):
                        for m in DFS(expression, k + 1, j):
                            output.append(l - m)
                elif expression[k] == "+":
                    for l in DFS(expression, i, k - 1):
                        for m in DFS(expression, k + 1, j):
                            output.append(l + m)
            if output:
                return output
            else:
                return [int(expression[i:j+1])]
                
        n = len(expression)
        return DFS(expression,0,n-1)