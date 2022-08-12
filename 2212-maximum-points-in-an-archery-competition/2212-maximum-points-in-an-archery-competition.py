class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        def DFS(bobArrows, score, numArrows,idx):
            nonlocal out,maxim
            if score > maxim:
                maxim = score
                out = [i for i in bobArrows]

            for i in range(idx,n):
                req = aliceArrows[i] + 1
                if numArrows >= req:
                    bobArrows[i] += req
                    DFS(bobArrows, score + i, numArrows - req,i+1)
                    bobArrows[i] -= req

        n,maxim,out = 12,0,[]
        bobArrows = [0] * n
        DFS(bobArrows, 0, numArrows,0)
        if sum(out) != numArrows: out[0] += numArrows - sum(out)
        return out