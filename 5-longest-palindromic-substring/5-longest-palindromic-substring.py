class Solution:
    def longestPalinOdd(self,s,n):
        ans = ""
        maxLen = 0
        for i in range(n-1):
            r = i+1
            l = i-1
            if 1 > maxLen:
                maxLen = 1
                ans = s[i]
            while l >= 0 and r < n:
                if s[l] != s[r]:
                    break
                if r-l+1 > maxLen:
                    maxLen = r-l+1
                    ans = s[l:r+1]
                l -= 1
                r += 1
        return ans,maxLen
    
    def longestPalinEven(self,s,n):
        ans = ""
        maxLen = 0
        for i in range(n-1):
            j = i+1
            r = i+2
            l = i-1
            if s[i] == s[j]:
                if 2 > maxLen:
                    maxLen = 2
                    ans = s[i:j+1]
                while l >= 0 and r < n:
                    if s[l] != s[r]:
                        break
                    if r-l+1 > maxLen:
                        maxLen = r-l+1
                        ans = s[l:r+1]
                    l -= 1
                    r += 1
        return ans,maxLen
    
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1: return s[0]
        ans1,len1 = self.longestPalinOdd(s,n)
        ans2,len2 = self.longestPalinEven(s,n)
        if len1 >= len2:
            return ans1
        return ans2