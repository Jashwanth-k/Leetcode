class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])
        r, c = 0, 0
        st = 0
        ans = []
        while r < n and c < m:
            if st == 0:
                while r >= 0 and c < m:
                    ans.append(mat[r][c])
                    r -= 1
                    c += 1
                r += 1
                c -= 1
                if c + 1 < m: c += 1
                else: r += 1
            if st == 1:
                while r < n and c >= 0:
                    ans.append(mat[r][c])
                    r += 1
                    c -= 1
                r -= 1
                c += 1
                if r + 1 < n: r += 1
                else: c += 1
            st = (st + 1) % 2
        return ans