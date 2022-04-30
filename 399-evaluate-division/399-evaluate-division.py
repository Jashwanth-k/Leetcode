class Solution:
    def BFS(self,equations,si,ei,d):
        q = collections.deque()
        q.append([si,1])
        visited = set()
        visited.add(si)
        
        while q:
            currNode,prevVal = q.popleft()
            if currNode == ei:
                return prevVal
            
            for sib,dist in d[currNode]:
                if sib not in visited:
                    val = prevVal * dist
                    q.append([sib,val])
                    visited.add(sib)
        return -1
        
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = collections.defaultdict(list)
        n = len(equations)
        for i in range(n):
            A,B = equations[i]
            val = values[i]
            d[A].append([B,val])
            
            num,den = val.as_integer_ratio()
            newVal = den / num
            d[B].append([A,newVal])
    
        output = []
        for i,j in queries:
            if i not in d or j not in d:
                output.append(-1)
            else:
                ans = self.BFS(equations,i,j,d)
                output.append(ans)
        return output