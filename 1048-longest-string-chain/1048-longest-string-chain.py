class Solution:
    def validate(self,prev,curr):
        a = 0
        b = 0
        m,n = len(curr),len(prev)
        if m-n != 1:
            return False
        while a < m and b < n:
            s1 = curr[a]
            s2 = prev[b]
            if s1 == s2:
                a += 1
                b += 1
            else:
                a += 1
        if a == b or a - b == 1:
            return True
        return False
    
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words,key = len)
        def chainHelper(words,i,n,prev,dp):
            if i >= n:
                return 0
            if dp[i][prev+1] != -1:
                return dp[i][prev+1]
            
            take = 0
            if prev == -1 or self.validate(words[prev],words[i]):
                take = 1 + chainHelper(words,i+1,n,i,dp)
            untake = chainHelper(words,i+1,n,prev,dp)
            dp[i][prev+1] = max(take,untake)
            return dp[i][prev+1]
        
        n = len(words)
        dp = [[-1]*(n+1) for j in range(n)]
        return chainHelper(words,0,n,-1,dp)