import queue
class Solution:
    def BFS(self,sv,d,visited):
        q = queue.Queue()
        q.put(sv)
        visited[sv] = True
        
        while not q.empty():
            curr = q.get()
            for sib in d[curr]:
                if visited[sib] == False:
                    visited[sib] = True
                    q.put(sib)
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        d = collections.defaultdict(list)
        n = len(isConnected)
        
        for i in range(n):
            sublist = isConnected[i]
            for j in range(n):
                if i != j:
                    if sublist[j] == 1:
                        d[i+1].append(j+1)
            
        visited = [False] * (n+1)
        c = 0
        for i in range(1,n+1):
            if visited[i] == False:
                c += 1
                self.BFS(i,d,visited)
        return c
                