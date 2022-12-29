#User function Template for python3
from sortedcontainers import SortedList
from bisect import bisect_left

class Solution:
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        jobs = []
        end = 0
        for i in range(n):
            jobs.append([Jobs[i].deadline,Jobs[i].profit])
            end = max(end,jobs[-1][0])
        used = SortedList([i for i in range(1,end+2)])
        jobs.sort(key = lambda x:x[1],reverse = True)
        res = ct = 0
        for deadline,profit in jobs:
            idx = bisect_left(used,deadline)
            if idx == len(used):
                continue
            if used[idx] != deadline:
                idx -= 1
            if idx < 0:
                continue
            used.discard(used[idx])
            res += profit
            ct += 1
        return [ct,res]

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha
class Job:
    '''
    Job class which stores profit and deadline.
    '''
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        info = list(map(int,input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3*i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit=info[3*i+2]
        ob = Solution()
        res = ob.JobScheduling(Jobs,n)
        print (res[0], end=" ")
        print (res[1])
# } Driver Code Ends