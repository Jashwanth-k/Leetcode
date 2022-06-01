class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n,m = len(mat),len(mat[0])
        def sortDiagonalCol(c):
            helper = []
            for j in range(max(n,m)):
                if c+j == m or j == n:
                    break
                helper.append(mat[j][c+j])
            helper.sort()
            return helper
        def sortDiagonalRow(r):
            helper = []
            for j in range(max(n,m)):
                if r+j == n or j == m:
                    break
                helper.append(mat[r+j][j])
            helper.sort()
            return helper
        
        for c in range(m):
            helper = sortDiagonalCol(c)
            for j in range(max(n,m)):
                if c+j == m or j == n:
                    break
                mat[j][c+j] = helper.pop(0)
        
        for r in range(n):
            helper = sortDiagonalRow(r)
            for j in range(max(n,m)):
                if r+j == n or j == m:
                    break
                mat[r+j][j] = helper.pop(0)
        return mat