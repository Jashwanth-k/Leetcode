class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        def keyError():
            return "?"
        
        n = len(s)
        d = collections.defaultdict(keyError)
        for i,j in knowledge:
            d["(" + i + ")"] = j
        
        prev = None
        ans = ""
        for i in range(n):
            if s[i] == "(":
                prev = i
            if prev == None:
                ans += s[i]
            elif s[i] == ")":
                ans += d[s[prev:i + 1]]
                prev = None
        return ans