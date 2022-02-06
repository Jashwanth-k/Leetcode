class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        if len(s) == 0:
            return [""]
        
        smalloutput = self.letterCasePermutation(s[1:])
        output = []
        for substr in smalloutput:
            if (48 <= ord(s[0]) <= 57):
                output += [s[0] + substr]
            else:
                output += [s[0].upper() + substr] + [s[0].lower() + substr]
        return output