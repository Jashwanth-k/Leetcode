import queue
class Solution:
    def BFS(self,sv,d,visited):
        q = queue.Queue()
        q.put(sv)
        visited.add(sv)
        while not q.empty():
            curr = q.get()
            for sib in d[curr]:
                if sib not in visited:
                    visited.add(sib)
                    q.put(sib)
    
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        d = defaultdict(list)
        for u,v in connections:
            d[u].append(v)
            d[v].append(u)
        
        connectedcom = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                connectedcom += 1
                self.BFS(i,d,visited)
        return connectedcom-1