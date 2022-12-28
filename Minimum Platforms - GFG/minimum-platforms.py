#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        overlaping = [0]*2361
        for i in range(n):
            overlaping[arr[i]] += 1
            overlaping[dep[i]+1] -= 1
        res = 1
        for i in range(1,2361):
            overlaping[i] = overlaping[i] + overlaping[i-1]
            res = max(res,overlaping[i])
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
# } Driver Code Ends