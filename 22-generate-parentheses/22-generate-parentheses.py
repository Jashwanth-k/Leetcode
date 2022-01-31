class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
            
        smalloutput = self.generateParenthesis(n-1)
        output = []
        
        for subpar in smalloutput:
            for j in range(len(subpar)):
                ans = subpar[:j] + '()' + subpar[j:]
                if ans not in output:
                    output.append(ans)
        return output
        