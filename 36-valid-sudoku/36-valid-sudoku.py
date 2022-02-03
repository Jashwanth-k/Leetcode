class Solution:
    def validate(self,board,r,c,n,nbr):
        # checking row
        for i in range(n):
            if i != c and board[r][i] == nbr:
                return True
            
        # checking column
        for i in range(n):
            if i != r and board[i][c] == nbr:
                return True
            
        # checking 3x3 sub-box
        subrow = r // 3 * 3
        subcol = c // 3 * 3
        for i in range(3):
            for j in range(3):
                if (subrow+i != r and subcol+j != c) and board[subrow + i][subcol + j] == nbr:
                    return True
        return False
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        for i in range(n):
            for j in range(n):
                if board[i][j] != '.' and self.validate(board,i,j,n,board[i][j]):
                    return False
        return True