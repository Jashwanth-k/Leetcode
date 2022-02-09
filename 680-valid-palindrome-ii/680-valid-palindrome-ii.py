class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        
        l,r = 0,len(s)-1
        while l < r and s[l] == s[r]:
            l += 1
            r -= 1
        
        substr = s[l+1:r+1]
        if substr == substr[::-1]:
            return True
        
        substr = s[l:r]
        if substr == substr[::-1]:
            return True
        return False