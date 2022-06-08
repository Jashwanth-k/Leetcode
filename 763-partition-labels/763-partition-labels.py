class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        def DFS(s,i,j):
            if i == j:
                return [1]
            if (i,j) in dp:
                return dp[i,j]
            
            ans1 = ans2 = []
            for k in range(i,j):
                if not set(s[i:k+1]) & set(s[k+1:j+1]):
                    left = DFS(s,i,k)
                    right = DFS(s,k+1,j)
                    curr = left + right
                    ans1 = curr
            else:
                ans2 = [len(s[i:j+1])]
            dp[i,j] = max(ans1,ans2,key=len)
            return dp[i,j]
                    
        n = len(s)
        dp = {}
        return DFS(s,0,n-1)