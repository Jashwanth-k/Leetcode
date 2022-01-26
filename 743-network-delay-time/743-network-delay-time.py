import queue
class Solution:
    def BFS(self,k,d,times,dist):
        q = queue.Queue()
        q.put(k)
        dist[k] = 0
        
        while not q.empty():
            curr = q.get()
            for sib,wt in d[curr]:
                if dist[curr] + wt < dist[sib]:
                    dist[sib] = dist[curr] + wt
                    q.put(sib)
        return
    
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d = collections.defaultdict(list)
        for i,j,w in times:
            d[i].append((j,w))
        
        dist = [float('inf')] * (n+1)
        self.BFS(k,d,times,dist)
        
        maxim = float('-inf')
        dist.pop(0)
        for i in dist:
            if i == float('inf'):
                return -1
            maxim = max(maxim,i)
        return maxim
        