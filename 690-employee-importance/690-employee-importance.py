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
        def DFS(sv):
            sib,imp = d[sv]
            dist[sv] = 0
            for j in sib:
                dist[sv] += DFS(j)
            dist[sv] += imp
            return dist[sv]
        
        d = collections.defaultdict(list)
        for i in employees:
            d[i.id].extend((i.subordinates,i.importance))
            
        dist = {}
        DFS(id)
        return dist[id]
