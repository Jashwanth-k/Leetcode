class Solution:
    def lcs(self,dp,n,m,str1,str2):
        for i in range(1,n+1):
            for j in range(1,m+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return 
        
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n,m = len(str1),len(str2)
        dp = [[0]*(m+1)for j in range(n+1)]
        self.lcs(dp,n,m,str1,str2)
        
        i,j = n,m
        ans = ""
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                ans += str1[i-1]
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                ans += str1[i-1]
                i -= 1
            else:
                ans += str2[j-1]
                j -= 1
        ans += str1[:i][::-1]
        ans += str2[:j][::-1]
        return ans[::-1]
                
                