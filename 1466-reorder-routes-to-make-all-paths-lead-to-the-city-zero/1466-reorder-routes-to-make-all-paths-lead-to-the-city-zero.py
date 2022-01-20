import queue
class Solution:    
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def DFS(sv):
            nonlocal c
            visited[sv] = True
            for sib,diff in d[sv]:
                if visited[sib] == False:
                    c += diff
                    DFS(sib)
                    
        d = collections.defaultdict(list)
        for i,j in connections:
            d[i].append((j,1))
            d[j].append((i,0))
            
        visited = [False] * n
        c = 0
        DFS(0)
        return c