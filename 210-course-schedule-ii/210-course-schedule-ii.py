import queue
class Solution:
    def BFS(self,q,d,deg,topo):
        while not q.empty():
            curr = q.get()
            topo.append(curr)
            
            for sib in d[curr]:
                deg[sib] -= 1
                if deg[sib] == 0:
                    q.put(sib)
                
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        d = collections.defaultdict(list)
        for u,v in prerequisites:
            d[u].append(v)
        
        deg = [0] * numCourses
        for i in d:
            for sib in d[i]:
                deg[sib] += 1
        
        topo = []
        q = queue.Queue()
        for j in range(numCourses):
            if deg[j] == 0:
                q.put(j)
                
        self.BFS(q,d,deg,topo)
        if len(topo) != numCourses:
            return []
        return topo[::-1]