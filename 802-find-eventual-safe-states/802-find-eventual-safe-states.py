class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        status = [0] * n
        res = []
        
        def dfs(i):
            if status[i] == 'visited':
                return True
            if status[i] == 'safe':
                return False
            status[i] = 'visited'
            for j in graph[i]:
                if dfs(j):
                    return True
            status[i] = 'safe'
            return False
        
        for i in range(n):
            if not dfs(i):
                res.append(i)
        return res