class Solution:
    def isCyclicDFS(self,sv,v,dv,graph):
        if v[sv] == 'safe':
            return

        v[sv] = 'visited'
        dv.add(sv)
        for sib in graph[sv]:
            if v[sib] == 0:
                if self.isCyclicDFS(sib,v,dv,graph):
                    v[sv] = 'cycle'
                    return True
            elif v[sib] == 'cycle' or v[sib] == 'visited':
                v[sv] = 'cycle'
                return True
            else:
                if sib in dv:
                    v[sib] = 'cycle'
                    return True
        dv.remove(sv)
        v[sv] = 'safe'
    
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        n = len(graph)
        v = [0] * n
        res = []
        for i in range(n):
            if not self.isCyclicDFS(i,v,set(),graph):
                res.append(i)
        return res
                
