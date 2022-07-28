class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = ""
        d = dict([[i+1,j] for i,j in enumerate(string.ascii_lowercase)])
        for n in range(n,0,-1):
            nbr = 26 if k >= 26 and k - 26 >= n-1 else k - (n-1)
            k -= nbr
            res += d[nbr]
        return res[::-1]