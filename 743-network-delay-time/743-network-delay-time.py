import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d = collections.defaultdict(list)
        for i,j,w in times:
            d[i].append((j,w))
            
        dist = [float('inf')]*(n+1)
        dist[k] = 0
        heap = [(0,k)]
        while heap:
            curr = heapq.heappop(heap)
            ndis,node = curr[0],curr[1]
            for sib,wt in d[node]:
                currdis = ndis + wt
                if currdis < dist[sib]:
                    dist[sib] = currdis
                    heapq.heappush(heap,(currdis,sib))
        dist.pop(0)
        ans = max(dist)
        return -1 if ans == float('inf') else ans