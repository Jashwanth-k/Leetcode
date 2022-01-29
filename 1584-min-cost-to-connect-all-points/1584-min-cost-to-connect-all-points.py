import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        d = collections.defaultdict(list)
        n = len(points)
        for i in range(n):
            for j in range(i+1,n):
                x,y = points[i],points[j]
                wt = abs(x[0] - y[0]) + abs(x[1] - y[1])
                d[i].append((j,wt))
                d[j].append((i,wt))
                
        key = [float('inf')] * n
        mst = [False] * n
        key[0] = 0
        heap = [(0, 0)]
        
        while heap:
            curr = heapq.heappop(heap)
            node = curr[1]
            if mst[node] == False:
                mst[node] = True

                for sib, wt in d[node]:
                    if mst[sib] == False and wt < key[sib]:
                        key[sib] = wt
                        heapq.heappush(heap,(wt, sib))

        return sum(key)