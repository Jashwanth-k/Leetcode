class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        top = left = 0
        right = down = n-1
        nbr = 1
        direction = 0
        matrix = [[0 for i in range(n)] for j in range(n)]
        
        while top <= down and left <= right:
            if direction == 0:
                for i in range(left,right+1):
                    matrix[top][i] = nbr
                    nbr += 1
                top += 1
            
            elif direction == 1:
                for i in range(top,down+1):
                    matrix[i][right] = nbr
                    nbr += 1
                right -= 1
            
            elif direction == 2:
                for i in range(right,left-1,-1):
                    matrix[down][i] = nbr
                    nbr += 1
                down -= 1
                
            elif direction == 3:
                for i in range(down,top-1,-1):
                    matrix[i][left] = nbr
                    nbr += 1
                left += 1
                
            direction = (direction+1)%4
        return matrix
                    