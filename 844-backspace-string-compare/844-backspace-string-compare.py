class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        n,m = len(s),len(t)
        def buildStr(s):
            ct = 0
            newStr = ""
            for i in s[::-1]:
                if i == "#":
                    ct += 1
                elif ct > 0:
                    ct -= 1
                else:
                    newStr += i
            return newStr
                
        newS = buildStr(s)
        newT = buildStr(t)
        return newS == newT