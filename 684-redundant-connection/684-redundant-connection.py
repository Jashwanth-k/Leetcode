class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def dfs(u,v):
            visited = set()
            stack = [u]
            while stack:
                node = stack.pop()
                if node == v:
                    return True
                visited.add(node)

                for nei in d[node]:
                    if nei not in visited:
                        stack.append(nei)
            return False

        d = defaultdict(list)

        redundant = []
        for u, v in edges:
            if u in d and v in d:
                if dfs(u,v):
                    redundant.append(u)
                    redundant.append(v)
            d[u].append(v)
            d[v].append(u)
        return redundant