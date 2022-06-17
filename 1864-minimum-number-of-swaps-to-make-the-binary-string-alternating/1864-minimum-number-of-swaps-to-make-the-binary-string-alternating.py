class Solution:
    def minSwaps(self, s: str) -> int:
        def compare(si,ei):
            substr,ans = "",0
            for i in range(max(ct)):
                substr += si + ei
            for i in range(len(s)):
                if substr[i] != s[i]:
                    ans += 1
            return ans
            
        ct = [0,0]
        for i in s:
            ct[ord(i)-48] += 1
        if abs(ct[0] - ct[1]) > 1:  return -1
        si = str(ct.index(max(ct)))
        ei = str(1 - int(si))
        ans = compare(si,ei)
        
        if ct[0] == ct[1]:
            return min(compare("0","1"),compare("1","0")) // 2
        return ans // 2