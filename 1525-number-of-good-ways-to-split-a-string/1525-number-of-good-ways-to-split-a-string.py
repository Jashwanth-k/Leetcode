class Solution:
    def numSplits(self, s: str) -> int:
        def calUniqChr(si,ei,inc):
            arr,d = [0]*n,set()
            for i in range(si,ei,inc):
                curr = s[i]
                d.add(curr)
                arr[i] = len(d)
            return arr
                
        n = len(s)
        prefix = calUniqChr(0,n,1)
        suffix = calUniqChr(n-1,-1,-1)
        ans = 0
        for i in range(n-1):
            if prefix[i] == suffix[i+1]:
                ans += 1
        return ans