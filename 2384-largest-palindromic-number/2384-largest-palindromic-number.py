class Solution:
    def largestPalindromic(self, num: str) -> str:
        if num == "0"*len(num): return "0"
        freq = Counter(num)
        mid = ""
        for i in freq:
            if freq[i] == 1 or freq[i] % 2 != 0: mid = max(mid,i)
        
        helper = [[i,freq[i]] for i in freq if freq[i] != 1]
        n = len(helper)
        helper.sort()
        for k in range(n):
            i,j = helper[k]
            if k == n-1 and i == "0": continue
            half = j // 2
            mid = (i*half) + mid + (i*half)
        return mid