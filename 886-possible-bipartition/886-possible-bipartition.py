import queue
class Solution:
    def BFS(self,sv,d,color):
        q = queue.Queue()
        q.put(sv)
        color[sv] = 1
        while not q.empty():
            node = q.get()
            for sib in d[node]:
                if color[sib] == -1:
                    color[sib] = 1 - color[node]
                    q.put(sib)
                else:
                    if color[node] == color[sib]:
                        return True
        return  
    
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        d = collections.defaultdict(list)
        for i,j in dislikes:
            d[i].append(j)
            d[j].append(i)
            
        color = [-1] * (n+1)
        for i in range(1,n+1):
            if color[i] == -1:
                if self.BFS(i,d,color):
                    return False
        return True