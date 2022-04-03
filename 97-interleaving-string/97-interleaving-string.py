class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def interHelper(s1,s2,s3,i,j,k,dp):
            if i < 0 and j < 0 and k < 0:
                return True
            if k < 0:
                return False
            if i < 0:
                if s2[:j+1] == s3[:k+1]:
                    return True
                return False
            if j < 0:
                if s1[:i+1] == s3[:k+1]:
                    return True
                return False
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if s1[i] == s3[k] and s2[j] == s3[k]:
                dp[i][j] = interHelper(s1,s2,s3,i-1,j,k-1,dp) or interHelper(s1,s2,s3,i,j-1,k-1,dp)
                return dp[i][j]
            
            add1 = add2 = False
            if s1[i] == s3[k]:
                add1 = interHelper(s1,s2,s3,i-1,j,k-1,dp)
            if s2[j] == s3[k]:
                add2 = interHelper(s1,s2,s3,i,j-1,k-1,dp)
            dp[i][j] = add1 or add2
            return dp[i][j]
        
        n,m,k = len(s1),len(s2),len(s3)
        dp = [[-1]*(m) for j in range(n)]
        return interHelper(s1,s2,s3,n-1,m-1,k-1,dp)