class Solution:
    def DFS(self,d,si,visited):
        visited.add(si) 
        curr = 0
        for sib in d[si]:
            if sib not in visited:
                curr += 1 + self.DFS(d,sib,visited)
        return curr
    
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        d = collections.defaultdict(list)
        for i in range(n):
            r1,c1,d1 = bombs[i]
            for j in range(n):
                if i == j: continue
                r2,c2,d2 = bombs[j]
                if (r1-r2)**2 + (c1-c2)**2 <= d1**2:
                    d[i].append(j)
        
        ans = 0
        for i in range(n):
            visited = set()
            curr = 1 + self.DFS(d, i, visited)
            ans = max(ans,curr)
        return ans
