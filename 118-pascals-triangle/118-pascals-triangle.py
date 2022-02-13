class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        smalloutput = self.generate(numRows-1)
        suboutput = smalloutput[numRows-2]
        ans = [0] * numRows
        ans[0],ans[-1] = suboutput[0],suboutput[-1]
        for i in range(1,len(suboutput)):
            ans[i] = suboutput[i] + suboutput[i-1]
            
        smalloutput.append(ans)
        return smalloutput
        