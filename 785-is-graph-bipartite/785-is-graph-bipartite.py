class Solution:
    def DFS(self,sv,graph,color):
        
        for sib in graph[sv]:
            if color[sib] == -1:
                color[sib] = 1 - color[sv]
                if self.DFS(sib,graph,color):
                    return True
            else:
                if color[sib] == color[sv]:
                    return True
        
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n
        
        for i in range(n):
            if color[i] == -1:
                color[i] = 1
                if self.DFS(i,graph,color):
                    return False
        return True
            
        