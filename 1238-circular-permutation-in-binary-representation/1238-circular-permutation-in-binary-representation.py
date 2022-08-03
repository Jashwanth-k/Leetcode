class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        def DFS(n):
            if n == 1:
                return ["0","1"]
            
            subans = DFS(n-1)
            res = []
            for i in range(len(subans)):
                res.append("0" + subans[i])
            for i in range(len(subans)-1,-1,-1):
                res.append("1" + subans[i])
            return res
        
        res = DFS(n)
        for i in range(2**n):
            if int(res[i],2) == start:
                return [int(j,2) for j in res[i:] + res[:i]]