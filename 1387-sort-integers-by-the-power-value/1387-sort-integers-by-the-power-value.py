import heapq
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def helper(n):
            if n == 1:
                return 0
            if n in dp:
                return dp[n]
            
            if n % 2 == 0:
                dp[n] = 1 + helper(n // 2)
                return dp[n]
            dp[n] = 1 + helper(n * 3 + 1)
            return dp[n]
        
        dp = {}
        minHeap = []
        for i in range(lo,hi+1):
            heapq.heappush(minHeap,[helper(i),i])
        ans = None
        for _ in range(k):
            ans = heapq.heappop(minHeap)
        return ans[1]