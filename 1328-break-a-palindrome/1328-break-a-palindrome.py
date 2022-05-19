class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1: return ""
        ans = "z"*n
        for i in range(n):
            for j in string.ascii_lowercase:
                right = n-1-i
                if i != right and j != palindrome[right]:
                    substr = palindrome[:i] + j + palindrome[i+1:]
                    ans = min(ans,substr)
        return ans