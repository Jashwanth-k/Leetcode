class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        factors,n = [],len(s)
        for i in range(1,int(math.sqrt(n))+1):
            if n % i == 0:
                factors += [i] + [n // i]
            
        for f in factors:
            if f == n: continue
            si,ei = 0,f
            prev = s[si:ei]
            flag = True
            while ei <= n:
                if s[si:ei] != prev:
                    flag = False
                    break
                si = ei
                ei += f
                    
            if flag: return True
        return False