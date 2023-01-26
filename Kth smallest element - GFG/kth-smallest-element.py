#User function Template for python3

class Solution:
    def kthSmallest(self,arr, l, r, k):
        if l > r:
            return
        mid = l + (r-l) // 2
        i = l
        pivot = arr[mid]
        arr[r],arr[mid] = arr[mid],arr[r]
        for j in range(l,r+1):
            if arr[j] < pivot:
                arr[i],arr[j] = arr[j],arr[i]
                i += 1
        arr[i],arr[r] = arr[r],arr[i]
        if k-1 == i:
            return arr[i]
        if k-1 > i:
            return self.kthSmallest(arr,i+1,r,k)
        return self.kthSmallest(arr,l,i-1,k)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    import random 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        k=int(input())
        ob=Solution()
        print(ob.kthSmallest(arr, 0, n-1, k))
        
# } Driver Code Ends