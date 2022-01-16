class Solution:
    def DFS(self,sv,vs,dvs,d):
        vs[sv] = True
        dvs[sv] = True
        for sib in d[sv]:
            if vs[sib] == False:
                if self.DFS(sib,vs,dvs,d):
                    return True
            else:
                if vs[sib] == True and dvs[sib] == True:
                    return True
        dvs[sv] = False
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        d = collections.defaultdict(list)
        for u,v in prerequisites:
            d[u] = d.get(u,[]) + [v]
        
        visited = [False] * numCourses
        dfsVisited = [False] * numCourses
        
        for i in range(numCourses):
            if visited[i] == False:
                if self.DFS(i,visited,dfsVisited,d):
                    return False
        return True
        