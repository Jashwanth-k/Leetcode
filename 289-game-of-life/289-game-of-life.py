class Solution:
    def checkCells(self,board,m,n,r,c,cell):
        count = 0
        
        if c+1 < n and board[r][c+1] == 1:
            count += 1
        if c-1 >= 0 and board[r][c-1] == 1:
            count += 1
        if r-1 >= 0 and board[r-1][c] == 1:
            count += 1
        if r+1 < m and board[r+1][c] == 1:
            count += 1
            
        if r-1 >= 0 and c+1 < n and board[r-1][c+1] == 1:
            count += 1
        if r+1 < m and c+1 < n and board[r+1][c+1] == 1:
            count += 1
        if r-1 >= 0 and c-1 >= 0 and board[r-1][c-1] == 1:
            count += 1
        if r+1 < m and c-1 >= 0 and board[r+1][c-1] == 1:
            count += 1
            
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
        
        for i in range(m):
            for j in range(n):
                if [i,j] in change:
                    board[i][j] = 1 - board[i][j]