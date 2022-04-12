class Solution:
    def validate(self,m,n,r,c):
        if r < 0 or c < 0:
            return False
        if r >= m or c >= n:
            return False
        return True
    
    def checkCells(self,board,m,n,r,c,cell):
        count = 0
        check = [[r,c+1],[r,c-1],[r-1,c],[r+1,c],[r-1,c+1],[r+1,c+1],[r-1,c-1],[r+1,c-1]]
        for k,l in check:
            if self.validate(m,n,k,l):
                count += board[k][l]
            
        if cell == 1:
            if count > 3 or count < 2:
                return True
            return False
        if count == 3:
            return True
        return False
        
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)
        n = len(board[0])
        change = []
        
        for i in range(m):
            for j in range(n):
                if self.checkCells(board,m,n,i,j,board[i][j]):
                    change.append([i,j])
        
        for [i,j] in change:
            board[i][j] = 1 - board[i][j]