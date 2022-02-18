class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagLen,strLen = len(p),len(s)
        if anagLen > strLen:
            return []
        i = j = 0
        output = []
        mapAnag = {}
        for k in p:
            mapAnag[k] = mapAnag.get(k,0) + 1
        count = len(mapAnag)
        
        while j < strLen:
            if s[j] in mapAnag:
                mapAnag[s[j]] -= 1
                if mapAnag[s[j]] == 0:
                    count -= 1
            
            if (j-i+1) == anagLen:
                if count == 0:
                    output.append(i)
                if s[i] in mapAnag:
                    if mapAnag[s[i]] == 0:
                        count += 1
                    mapAnag[s[i]] += 1
                i += 1
                j += 1
            else:
                j += 1
        return output