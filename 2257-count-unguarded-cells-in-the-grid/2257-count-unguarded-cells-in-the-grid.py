class Solution:
    def guardLookup(self, mat, m, n, i, j):
        mat[i][j] = 1
        # right
        for c in range(j+1,n):
            if mat[i][c] == 1:
                break
            mat[i][c] = 2

        # left
        for c in range(j-1,-1,-1):
            if mat[i][c] == 1:
                break
            mat[i][c] = 2

        #down
        for r in range(i+1,m):
            if mat[r][j] == 1:
                break
            mat[r][j] = 2

        #up
        for r in range(i-1,-1,-1):
            if mat[r][j] == 1:
                break
            mat[r][j] = 2
            
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        mat = [[-1]*(n) for j in range(m)]
        for i,j in walls + guards:
            mat[i][j] = 1
                        
        for i,j in guards:
            self.guardLookup(mat,m,n,i,j)
            
        count = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == -1:
                    count += 1
        return count