class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n,m = len(s1),len(s2)
        if n > m:
            return False
        i = j = 0
        dwindow = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        ds1 = {}
        for s in s1:
            ds1[s] = ds1.get(s,0) + 1
            
        while j < m:
            dwindow[s2[j]] += 1
            if (j-i+1) == n:
                for s in s1:
                    if dwindow[s] != ds1[s]:
                        break
                else:
                    return True
                dwindow[s2[i]] -= 1
                i += 1
                j += 1
            else:
                j += 1
        return False
        