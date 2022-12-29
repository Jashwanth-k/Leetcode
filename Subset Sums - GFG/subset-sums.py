#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
		def dfs(i,cursum = 0):
		    if i == N:
		        ans.append(cursum)
		        return
		    dfs(i+1,cursum + arr[i])
		    dfs(i+1,cursum)
		ans = []
		dfs(0)
		return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends