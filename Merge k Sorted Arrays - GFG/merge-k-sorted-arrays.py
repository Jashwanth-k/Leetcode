#User function Template for python3
from heapq import heappush,heappop
class Solution:
    #Function to merge k sorted arrays.
    def mergeKArrays(self, arr, K):
        def merge(left,right):
            n,m = len(left),len(right)
            arr = []
            i = j = 0
            while i < n and j < m:
                if left[i] <= right[j]:
                    arr.append(left[i])
                    i += 1
                else:
                    arr.append(right[j])
                    j += 1
            arr += left[i:]
            arr += right[j:]
            return arr
        
        def mergeSort(l,r):
            if l > r:
                return
            if l == r:
                return arr[l]
            mid = l + (r-l) // 2
            left = mergeSort(l,mid)
            right = mergeSort(mid+1,r)
            return merge(left,right)
            
        return mergeSort(0,K-1)
        
        
        
        
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