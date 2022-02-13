class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        prevrow = self.getRow(rowIndex-1)
        output = [prevrow[0]]
        for i in range(1,len(prevrow)):
            output.append(prevrow[i] + prevrow[i-1])
        output.append(prevrow[-1])
        return output
