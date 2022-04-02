class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        i,j = 0,n-1
        while i < j:
            if s[i] != s[j]:
                break
            i += 1
            j -= 1
        
        if i >= j:
            return True
        
        substr = s[:i] + s[i+1:]
        if substr == substr[::-1]:
            return True
        substr = s[:j] + s[j+1::]
        if substr == substr[::-1]:
            return True
        return False