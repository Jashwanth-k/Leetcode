class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        def jumpsHelper(arr,i,d,n,dp):
            if i == 0 and arr[i] <= arr[i+1]:
                return 1
            if i == n-1 and arr[i] <= arr[i-1]:
                return 1
            if i != 0 and i != n-1 and arr[i-1] >= arr[i] <= arr[i+1]:
                return 1
            if dp[i] != -1:
                return dp[i]
            
            ans = float('-inf')
            for jump in range(1,d+1):
                currans1 = float('-inf')
                if i + jump < n:
                    if arr[i] > arr[i+jump]:
                        currans1 = 1 + jumpsHelper(arr,i+jump,d,n,dp)
                    if arr[i] <= arr[i+jump]:
                        break
                ans = max(ans,currans1)
                        
            for jump in range(1,d+1):
                currans2 = float('-inf')
                if i - jump >= 0:
                    if arr[i] > arr[i-jump]:
                        currans2 = 1 + jumpsHelper(arr,i-jump,d,n,dp)
                    if arr[i] <= arr[i-jump]:
                        break
                ans = max(ans,currans2)
            dp[i] = ans
            return ans
        
        output = float('-inf')
        n = len(arr)
        if n == 1: return 1
        dp = [-1]*n
        for i in range(n):
            ans = jumpsHelper(arr,i,d,n,dp)
            output = max(output,ans)
        return output