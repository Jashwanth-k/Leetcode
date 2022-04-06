class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        def threeSumHelper(arr,target,i,cap,dp):
            if target == 0 and cap == 0:
                return 1
            if i < 0 or cap < 0:
                return 0
            if dp[i][cap][target] != -1:
                return dp[i][cap][target]
            
            inclu = 0
            if target >= arr[i]:
                inclu = threeSumHelper(arr,target-arr[i],i-1,cap-1,dp)
            exclu = threeSumHelper(arr,target,i-1,cap,dp)
            dp[i][cap][target] = (inclu + exclu) % (10**9 + 7)
            return dp[i][cap][target]
        
        n = len(arr)
        arr.sort()
        dp = [[[-1]*(target+1) for j in range(4)] for i in range(n)]
        return threeSumHelper(arr,target,n-1,3,dp)
    