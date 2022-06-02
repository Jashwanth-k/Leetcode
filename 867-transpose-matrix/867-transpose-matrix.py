class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        output = []
        n,m = len(matrix),len(matrix[0])
        for j in range(m):
            helper = []
            for i in range(n):
                helper.append(matrix[i][j])
            output.append(helper)
        return output