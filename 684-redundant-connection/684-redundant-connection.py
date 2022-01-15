class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def dfs(u,v,visited):
            visited.add(u)
            if u == v:
                return True
            for sib in d[u]:
                if sib not in visited:
                    if dfs(sib,v,visited):
                        return True
            return

        d = defaultdict(list)

        redundant = []
        for u, v in edges:
            if u in d and v in d:
                if dfs(u,v,set()):
                    redundant.append(u)
                    redundant.append(v)
            d[u].append(v)
            d[v].append(u)
        return redundant