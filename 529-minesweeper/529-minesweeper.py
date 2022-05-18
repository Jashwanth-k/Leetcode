class Solution:
    def checkMine(self,board,n,m,r,c):
        paths = [[r,c+1],[r,c-1],[r-1,c],[r+1,c],[r+1,c+1],[r-1,c+1],[r+1,c-1],[r-1,c-1]]
        ct = 0
        for i,j in paths:
            if 0 <= i < n and 0 <= j < m:
                if board[i][j] == "M":
                    ct += 1
        return ct
    
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def exploreBoard(baord,r,c,n,m):
            if baord[r][c] != "M" and baord[r][c] != "E":
                return
            if baord[r][c] == "M":
                baord[r][c] = "X"
                return
            
            curr = self.checkMine(board,n,m,r,c)
            board[r][c] = str(curr) if curr != 0 else "B"
            if baord[r][c] != "B":
                return
            paths = [[r,c+1],[r,c-1],[r-1,c],[r+1,c],[r+1,c+1],[r-1,c+1],[r+1,c-1],[r-1,c-1]]
            for i,j in paths:
                if 0 <= i < n and 0 <= j < m:
                    exploreBoard(board,i,j,n,m)
            return        
        
        n,m = len(board),len(board[0])
        exploreBoard(board,click[0],click[1],n,m)
        return board