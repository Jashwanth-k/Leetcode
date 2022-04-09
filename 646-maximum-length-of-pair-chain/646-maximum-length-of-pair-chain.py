class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs,key=lambda x:x[1])
        def chainHelper(pairs,i,prev,n,dp):
            if i == n:
                return 0
            if dp[i] != -1:
                return dp[i]
     
            inclu = 0
            if pairs[i][0] > prev:
                inclu = 1 + chainHelper(pairs,i+1,pairs[i][1],n,dp)
            exclu = chainHelper(pairs,i+1,prev,n,dp)
            dp[i] = max(exclu,inclu)
            return dp[i]
        
        n = len(pairs)
        dp = [-1]*n
        return chainHelper(pairs,0,float('-inf'),n,dp)