class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        mid = (n-1) // 2
        for i in range(mid+1):
            s[i],s[n-1-i] = s[n-1-i],s[i]