class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        def binarySearch(target):
            si,ei = 0,len(arr)-1
            while si <= ei:
                mid = si + (ei - si) // 2
                if target == arr[mid]:
                    return arr[mid]
                if target > arr[mid]:
                    si = mid+1
                else:
                    ei = mid-1
            return arr[si] if si != len(arr) else -1
        
        n = len(events)
        events.sort(key=lambda x:x[0])
        suffix = [0]*n
        maxim = 0
        for i in range(n-1,-1,-1):
            maxim = max(maxim,events[i][2])
            suffix[i] = maxim
        indices = {}
        for i in range(n):
            si = events[i][0]
            if si not in indices:
                indices[si] = i
        arr = list(indices.keys())
        
        ans = 0
        for st, ed, v in events:
            nbr = binarySearch(ed + 1)
            if nbr == -1:
                ans = max(ans, v)
            else:
                idx = indices[nbr]
                ans = max(ans,v + suffix[idx])
        return ans