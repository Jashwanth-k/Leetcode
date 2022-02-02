class Solution:
    def isSafe(self,row,col,n,board):            
        # UP
        i = row
        while i >= 0:
            if board[i][col] == 'Q':
                return False
            i -= 1
            
        # left-top diagonal
        i,j = row,col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
            
        # right-top diagonal
        i,j = row,col
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True
    
    def backtrack(self,row,n,board,output):
        if row == n:
            output[0] += 1
            return
        
        for col in range(n):
            if self.isSafe(row,col,n,board):
                board[row][col] = 'Q'
                self.backtrack(row+1,n,board,output)
                board[row][col] = '.'
        return
    
    def totalNQueens(self, n: int) -> int:
        board = [['.' for i in range(n)] for j in range(n)]
        output = [0]
        self.backtrack(0,n,board,output)
        return output[0]