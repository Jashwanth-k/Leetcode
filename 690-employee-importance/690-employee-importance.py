"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def DFS(sv,visited):
            visited.add(sv)
            sib,imp = d[sv]
            for j in sib:
                if j not in visited:
                    dist[sv] = dist.get(sv,0) + DFS(j,visited)
            dist[sv] = dist.get(sv,0) + imp
            return dist[sv]
        
        d = collections.defaultdict(list)
        for i in employees:
            d[i.id].extend((i.subordinates,i.importance))
        
        dist = {}
        DFS(id,set())
        return dist[id]