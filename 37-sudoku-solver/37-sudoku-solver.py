class Solution:
    def isSafe(self,board,r,c,n,nbr):
        # checking row
        for i in range(n):
            if i != c and board[r][i] == nbr:
                return False
            
        # checking column
        for i in range(n):
            if i != r and board[i][c] == nbr:
                return False
            
        # checking 3x3 sub-box
        subrow = r // 3 * 3
        subcol = c // 3 * 3
        for i in range(3):
            for j in range(3):
                if (subrow+i != r and subcol+j != c) and board[subrow + i][subcol + j] == nbr:
                    return False
        return True
    
    def solveSudokuHelper(self,board,r,c,n):
        if r >= n:
            return board
        
        while c < n and board[r][c] != '.':
            c += 1
            
        if c >= n:
            ans = self.solveSudokuHelper(board,r+1,0,n)
            if ans: return ans
            
        for i in range(1,10):
            nbr = str(i)
            if self.isSafe(board,r,c,n,nbr):
                board[r][c] = nbr
                ans = self.solveSudokuHelper(board,r,c+1,n)
                if ans: return ans
                board[r][c] = '.'
        return

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.solveSudokuHelper(board,0,0,9)
        
