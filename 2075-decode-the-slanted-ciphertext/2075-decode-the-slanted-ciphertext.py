class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        cols = n // rows
        ans = ""
        for i in range(cols):
            for j in range(i,n,cols+1):
                ans += encodedText[j]
        return ans.rstrip()