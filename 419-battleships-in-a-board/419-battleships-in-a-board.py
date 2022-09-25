class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def DFS(i,j):
            board[i][j] = "."
            for r,c in [[0,1],[0,-1],[1,0],[-1,0]]:
                ni,nj = i + r,j + c
                if 0 <= ni < n and 0 <= nj < m and board[ni][nj] == "X":
                    DFS(ni,nj)
            
        n,m = len(board),len(board[0])
        res = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == "X":
                    DFS(i,j)
                    res += 1
        return res