class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        d = collections.defaultdict(list)
        for i,j,k in edges:
            d[i].append((j,k))
            d[j].append((i,k))
            
        s = collections.defaultdict(list)
        for i in range(n):
            heap = [(0, i)]
            dist = [float('inf')] * n
            dist[i] = 0
            while heap:
                curr = heap.pop(0)
                ndis, node = curr[0], curr[1]
                for sib, wt in d[node]:
                    currdis = ndis + wt
                    if currdis < dist[sib] and currdis <= distanceThreshold:
                        if sib not in s[i]: s[i].append(sib)
                        dist[sib] = currdis
                        heapq.heappush(heap, (currdis, sib))
        
        maxim = float('inf')
        ans = float('-inf')
        for i in range(n):
            if len(s[i]) <= maxim:
                maxim = len(s[i])
                ans = max(ans,i)
        return ans