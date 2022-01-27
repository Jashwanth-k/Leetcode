import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        d = collections.defaultdict(list)
        m = len(edges)
        for i in range(m):
            edge = edges[i]
            succ = succProb[i]
            a, b = edge[0], edge[1]
            d[a].append((b,succ))
            d[b].append((a,succ))
            
        dist = [float('-inf')] * (n)
        dist[start] = 1
        heap = [(1, start)]
        while heap:
            curr = heapq._heappop_max(heap)
            ndist,node = curr[0], curr[1]
            for sib, wt in d[node]:
                if ndist * wt > dist[sib]:
                    dist[sib] = ndist * wt
                    heap.append((dist[sib], sib))
                    heapq._siftdown_max(heap,0,len(heap)-1)
        
        if dist[end] == float('-inf'):
            return 0
        return dist[end]
                    
        