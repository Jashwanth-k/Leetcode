class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n,m = len(s),len(p)
        if m > n: return []
        i = j = 0
        output = []
        dwindow = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        danag = {}
        for k in p:
            danag[k] = danag.get(k,0) + 1
            
        while j < n:
            dwindow[s[j]] += 1
            if (j-i+1) == m:
                for k in p:
                    if dwindow[k] != danag[k]:
                        break
                else:
                    output.append(i)
                dwindow[s[i]] -= 1
                i += 1
                j += 1
            else:
                j += 1
        return output