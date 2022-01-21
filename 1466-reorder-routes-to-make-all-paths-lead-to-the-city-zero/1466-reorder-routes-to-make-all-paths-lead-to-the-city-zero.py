class Solution:    
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def DFS(sv):
            nonlocal c
            visited[sv] = True
            for sib,check in d[sv]:
                if visited[sib] == False:
                    if check:
                        c += 1
                    DFS(sib)
                    
        d = collections.defaultdict(list)
        for i,j in connections:
            d[i].append((j,True))
            d[j].append((i,False))
            
        visited = [False] * n
        c = 0
        DFS(0)
        return c
