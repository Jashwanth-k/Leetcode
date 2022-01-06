class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        n = len(box)
        m = len(box[0])
        d = {}
        for i in range(n):
            r = m-1
            l = r-1
            while r >= l and l >= 0:
                if box[i][l] == "#" and box[i][r] == ".":
                    box[i][l],box[i][r] = box[i][r],box[i][l]
                elif box[i][l] == '.' and box[i][r] == '.':
                    l -= 1
                elif box[i][l] == '*':
                    r = l-1
                    l = r-1
                else:
                    r -= 1
                    l = r-1

        output = [["" for i in range(n)]for j in range(m)]
        for i in range(n):
            for j in range(m):
                output[j][n-i-1] = box[i][j]
        return output