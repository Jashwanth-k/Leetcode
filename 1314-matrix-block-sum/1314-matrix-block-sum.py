class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(mat),len(mat[0])
        output = [[0]*(n) for j in range(m)]
        for i in range(m):
            for j in range(n):
                rsi = max(0,i-k)
                rei = min(m-1,i+k)
                csi = max(0,j-k)
                cei = min(n-1,j+k)
                curr = 0
                for r in range(rsi,rei+1):
                    for c in range(csi,cei+1):
                        curr += mat[r][c]
                output[i][j] = curr
        return output