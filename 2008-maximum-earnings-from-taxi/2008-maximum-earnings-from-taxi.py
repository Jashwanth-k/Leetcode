class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        def binarySearch(si,ei,target):
            while si <= ei:
                mid = si + (ei - si) // 2
                if target > rides[mid][0]:
                    si = mid + 1
                else:
                    ei = mid - 1
            return si
            
        def DFS(i):
            if i == rlen:
                return 0
            if (i) in dp:
                return dp[i]
            
            st,ed,v = rides[i]
            idx = binarySearch(i+1,rlen-1,ed)
            pick = ed + v - st + DFS(idx)
            unpick = DFS(i+1)
            dp[i] = max(pick,unpick)
            return dp[i]
            
        rlen = len(rides)
        rides.sort(key=lambda x:x[0])
        dp = {}
        return DFS(0)