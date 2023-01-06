#User function Template for python3


#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
from collections import *
def graphColoring(graph, k, V):
    def helper():
        return []
    
    def dfs(node):
        if node == n:
            return True
        
        for j in range(k):
            if all(color[sib] != j for sib in d[node]):
                color[node] = j
                if dfs(node + 1):
                    return True
                color[node] = -1
        return False
    
    n = len(graph)
    color = [-1]*n
    d = defaultdict(helper)
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                d[i].append(j)
    return dfs(0)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        V = int(input())
        k = int(input())
        m = int(input())
        list = [int(x) for x in input().strip().split()]
        graph = [[0 for i in range(V)] for j in range(V)]
        cnt = 0
        for i in range(m):
            graph[list[cnt]-1][list[cnt+1]-1]=1
            graph[list[cnt+1]-1][list[cnt]-1]=1
            cnt+=2
        if(graphColoring(graph, k, V)==True):
            print(1)
        else:
            print(0)

        t = t-1

# } Driver Code Ends