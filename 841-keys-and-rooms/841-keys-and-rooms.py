import queue
class Solution:
    def BFS(self,d,visited):
        visited[0] = True
        q = queue.Queue()
        q.put(0)
        while not q.empty():
            curr = q.get()
            for sib in d[curr]:
                if visited[sib] == False:
                    visited[sib] = True
                    q.put(sib)
                    
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        d = collections.defaultdict(list)
        n = len(rooms)
        for i in range(n):
            for j in rooms[i]:
                d[i].append(j)
                
        visited = [False] * n
        for i in range(n):
            if visited[i] == False:
                self.BFS(d,visited)
                
        for i in visited:
            if i == False:
                return False
        return True
                