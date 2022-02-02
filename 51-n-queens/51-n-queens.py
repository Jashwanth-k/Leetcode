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
            helper = []
            for j in board:
                helper.append("".join(j))
            output.append(helper)
            return
        
        for col in range(n):
            if self.isSafe(row,col,n,board):
                board[row][col] = 'Q'
                self.backtrack(row+1,n,board,output)
                board[row][col] = '.'
        return
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for i in range(n)] for j in range(n)]
        output = []
        self.backtrack(0,n,board,output)
        return output