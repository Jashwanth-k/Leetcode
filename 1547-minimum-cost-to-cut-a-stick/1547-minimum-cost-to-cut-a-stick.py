class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        def DFS(si, ei, csi, cei):
            if ei - si == 1 or cei == csi:
                return 0
            if (si,ei) in dp:
                return dp[si,ei]

            ans = float("inf")
            for k in range(csi,cei):
                curcut = cuts[k]
                left = DFS(si, curcut, csi, k)
                right = DFS(curcut, ei, k+1, cei)
                ans = min(ans,left + right + ei - si)
            dp[si,ei] = ans
            return dp[si,ei]
        
        m = len(cuts)
        cuts.sort()
        dp = {}
        return DFS(0, n, 0, m)