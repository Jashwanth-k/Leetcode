from collections import *
from heapq import heappush,heappop
class Solution:
	def topK(self, nums, k):
	    d = Counter(nums)
	    minHp = []
	    for i in d:
	        heappush(minHp,[d[i],i])
	        if len(minHp) > k:
	            heappop(minHp)
	    res = []
	    while minHp:
	        res.append(heappop(minHp)[1])
	    return res[::-1]

#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	a = list(map(int, input().strip().split()))
    	n = a[0]
    	nums = a[1:]
    	k = int(input().strip())
    	obj = Solution()
    	ans = obj.topK(nums, k)
    	for i in ans:
    		print(i, end = " ")
    	print()
# } Driver Code Ends