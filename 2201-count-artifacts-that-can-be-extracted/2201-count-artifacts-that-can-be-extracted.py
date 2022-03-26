class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        helper = [[0]*n for j in range(n)]
        count = 0
        for i,j in dig:
            helper[i][j] = 1
        
        for i,j,k,l in artifacts:
            flag = True
            for r in range(i,k+1):
                for c in range(j,l+1):
                    if helper[r][c] == 0:
                        flag = False
                        break
            if flag:
                count += 1
        return count
                