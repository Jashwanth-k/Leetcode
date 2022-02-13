class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        smalloutput = self.generate(numRows-1)
        suboutput = smalloutput[numRows-2]
        ans = [0] * numRows
        ans[0],ans[-1] = suboutput[0],suboutput[-1]
        i,j = 0,1
        while j < len(suboutput):
            ans[j] = suboutput[i] + suboutput[j]
            i += 1
            j += 1
            
        smalloutput.append(ans)
        return smalloutput
        