class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        r = n // rows
        if r == 0: return ""
        text = []
        i,j = 0,r
        while j <= n:
            text.append(encodedText[i:j])
            i = j
            j += r
        
        s = 0
        e = r
        ans = ""
        while s < e:
            c = s
            for substr in text:
                if c == r: break
                ans += substr[c]
                c += 1
            s += 1
        return ans.rstrip()
            