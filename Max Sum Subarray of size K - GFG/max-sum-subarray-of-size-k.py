#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        i = j = 0
        currSum = 0
        maxSum = float('-inf')
        while j < N:
            if (j-i+1) == K:
                currSum += Arr[j]
                maxSum = max(maxSum,currSum)
                currSum -= Arr[i]
                i += 1
                j += 1
            else:
                currSum += Arr[j]
                j += 1
        return maxSum

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends