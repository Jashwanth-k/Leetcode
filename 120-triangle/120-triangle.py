class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def minimumTotalHelper(triangle,dp,idx = 0,i = 0):
            if i == len(triangle)-1:
                return triangle[i][idx]
            
            if dp[i][idx] != -1:
                return dp[i][idx]
            
            left = triangle[i][idx] + minimumTotalHelper(triangle,dp,idx,i+1)
            right = triangle[i][idx] + minimumTotalHelper(triangle,dp,idx+1,i+1)
            dp[i][idx] = min(left,right)
            return dp[i][idx]
        
        dp = [[-1]*i for i in range(1,len(triangle)+1)]
        return minimumTotalHelper(triangle,dp)
            