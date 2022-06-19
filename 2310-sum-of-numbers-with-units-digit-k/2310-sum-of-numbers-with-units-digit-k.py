class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        arr = []
        for i in range(1,num+1):
            if i % 10 == k:
                arr.append(i)
                
        def DFS(i,k):
            if k == 0:
                return 0
            if i < 0:
                return float("inf")
            if (i,k) in dp:
                return dp[i,k]
        
            inclu = float("inf")
            if arr[i] <= k:
                inclu = 1 + DFS(i,k - arr[i])
            exclu = DFS(i-1,k)
            dp[i,k] = min(inclu,exclu)
            return dp[i,k]
        
        n = len(arr)
        dp = {}
        ans = DFS(n-1,num)
        return ans if ans != float("inf") else -1