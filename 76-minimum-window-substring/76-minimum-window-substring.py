class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        i = j = 0
        minLen = float('inf')
        output = ""
        d = {}
        for k in t:
            d[k] = d.get(k,0) + 1
        ct = len(d)
        
        while j < len(s):
            if s[j] in d:
                if d[s[j]] == 1:
                    ct -= 1
                d[s[j]] -= 1
            
            if ct == 0:
                while ct == 0:
                    if j-i+1 < minLen:
                        minLen = j-i+1
                        output = s[i:j+1]
                    if s[i] in d:
                        if d[s[i]] == 0:
                            ct += 1
                        d[s[i]] += 1
                    i += 1
            j += 1
        return output
                    