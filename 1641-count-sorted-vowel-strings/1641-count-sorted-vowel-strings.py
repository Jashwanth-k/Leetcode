class Solution:
    def countVowelStrings(self, n: int) -> int:
        def DFS(n):
            if n == 1:
                return ([1]*(5),5)
            
            subans,tsum = DFS(n-1)
            ans = [tsum]
            for i in subans:
                tsum -= i
                if not tsum: continue
                ans.append(tsum)
            return ans,sum(ans)
        return DFS(n)[1]