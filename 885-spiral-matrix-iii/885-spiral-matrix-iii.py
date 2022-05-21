class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        def validate(i,j):
            if (not 0 <= i < rows) or (not 0 <= j < cols):
                return False
            return True
        
        output = [[rStart,cStart]]
        dist = 0
        while len(output) != rows * cols:
            dist += 1
            #right
            for j in range(dist):
                cStart += 1
                if validate(rStart,cStart): output.append([rStart,cStart]) 
                    
            #down 
            for j in range(dist):
                rStart += 1
                if validate(rStart,cStart): output.append([rStart,cStart]) 
            
            dist += 1
            #left
            for j in range(dist):
                cStart -= 1
                if validate(rStart,cStart): output.append([rStart,cStart]) 
                    
            #top
            for j in range(dist):
                rStart -= 1
                if validate(rStart,cStart): output.append([rStart,cStart]) 
        return output
                