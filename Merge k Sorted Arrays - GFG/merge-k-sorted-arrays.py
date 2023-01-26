#User function Template for python3
from heapq import heappush,heappop
class Solution:
    #Function to merge k sorted arrays.
    def mergeKArrays(self, arr, K):
        helper = [0]*K
        minHp = []
        res = []
        for i in range(K):
            heappush(minHp,[arr[i][0],0,i])
        while minHp:
            cur,elidx,i = heappop(minHp)
            res.append(cur)
            if elidx + 1 == K:
                continue
            heappush(minHp,[arr[i][elidx+1],elidx+1,i])
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        numbers=[[ 0 for _ in range(n) ] for _ in range(n) ]
        line=input().strip().split()
        for i in range(n):
            for j in range(n):
                numbers[i][j]=int(line[i*n+j])
        ob = Solution();
        merged_list=ob.mergeKArrays(numbers, n)
        for i in merged_list:
            print(i,end=' ')
        print()
# } Driver Code Ends