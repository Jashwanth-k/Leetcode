#User function Template for python3

class Solution:
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        d = [None] * n
        for j in range(n):
            if d[j]:
                continue
            for i in range(n):
                if M[j][i] and M[i][j]:
                    d[j] = True
                    d[i] = True
                    continue
                elif M[j][i]:
                    d[j] = True
                    continue
        flag = idx = -1
        for i in range(n):
            if flag == d[i]:
                return -1
            if d[i] == None:
                flag = None
                idx = i
        return idx
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        ob = Solution()
        print(ob.celebrity(m,n))
# } Driver Code Ends