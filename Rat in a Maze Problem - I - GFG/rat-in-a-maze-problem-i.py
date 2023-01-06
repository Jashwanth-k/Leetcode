#User function Template for python3

class Solution:
    def findPath(self, m, n):
        def dfs(i,j,path):
            if i < 0 or j < 0 or i == n or j == n or m[i][j] == 0:
                return 
            if i == n-1 and j == n-1:
                res.append(path)
                return
            m[i][j] = 0
            dfs(i,j+1,path + "R")
            dfs(i,j-1,path + "L")
            dfs(i+1,j,path + "D")
            dfs(i-1,j,path + "U")
            m[i][j] = 1
            
        res = []
        dfs(0,0,"")
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends