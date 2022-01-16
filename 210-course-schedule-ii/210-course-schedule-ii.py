class Solution:
    def DFS(self,sv,vs,dvs,d,stack):
        vs[sv] = True
        dvs[sv] = True
        
        for sib in d[sv]:
            if vs[sib] == False:
                if self.DFS(sib,vs,dvs,d,stack) == True:
                    return True
            else:
                if vs[sib] == True and dvs[sib] == True:
                    return True
        dvs[sv] = False
        stack.append(sv)
                
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        d = collections.defaultdict(list)
        for u,v in prerequisites:
            d[u].append(v)
            
        vs = [False] * numCourses
        dvs = [False] * numCourses
        output = []
        stack = []
        
        for i in range(numCourses):
            if vs[i] == False:
                if self.DFS(i,vs,dvs,d,stack):
                    return []
        return stack