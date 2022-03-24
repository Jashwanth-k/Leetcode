class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        helper = []
        arrlen = len(strs)
        for i in range(arrlen):
            s = strs[i]
            d = { "0" : 0 , "1" : 0}
            for j in s: d[j] += 1
            helper.append(d)
            
        def maxFormHelper(strs,m,n,i,helper,dp):
            if i < 0:
                return 0
            
            if (i,m,n) in dp:
                return dp[i,m,n]
            
            submap = helper[i]
            pick = float('-inf')
            if submap["0"] <= m and submap["1"] <= n:
                pick = 1 + maxFormHelper(strs,m-submap["0"],n-submap["1"],i-1,helper,dp)
            unpick = maxFormHelper(strs,m,n,i-1,helper,dp)
            dp[i,m,n] = max(pick,unpick)
            return dp[i,m,n]
        
        dp = {}
        return maxFormHelper(strs,m,n,arrlen-1,helper,dp)