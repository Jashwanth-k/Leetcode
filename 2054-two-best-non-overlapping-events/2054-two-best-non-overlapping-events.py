class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        def binarySearch(target):
            si,ei = 0,n-1
            while si <= ei:
                mid = si + (ei - si) // 2
                if target == events[mid][0]:
                    ei = mid-1
                if target > events[mid][0]:
                    si = mid+1
                else:
                    ei = mid-1
            return si if si != n else -1
        
        n = len(events)
        events.sort(key=lambda x:x[0])
        suffix = [0]*n
        maxim = 0
        for i in range(n-1,-1,-1):
            maxim = max(maxim,events[i][2])
            suffix[i] = maxim
        
        ans = 0
        for st, ed, v in events:
            idx = binarySearch(ed + 1)
            if idx == -1:
                ans = max(ans, v)
            else:
                ans = max(ans,v + suffix[idx])
        return ans