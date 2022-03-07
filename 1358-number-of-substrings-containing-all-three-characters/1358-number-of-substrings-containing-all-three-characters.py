class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        i = j = 0
        n = len(s)
        d = {'a' : 1,'b' : 1,'c' : 1,}
        output = 0
        count = 3
        while j < n:
            d[s[j]] -= 1
            if d[s[j]] == 0:
                count -= 1
            if count == 0:
                while count == 0:
                    output += 1 + ((n-1) - j)
                    d[s[i]] += 1
                    if d[s[i]] == 1:
                        count += 1
                    i += 1
            j += 1
        return output
        