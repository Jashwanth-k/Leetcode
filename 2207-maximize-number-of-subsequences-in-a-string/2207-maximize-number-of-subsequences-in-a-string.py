class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        def countSubs(text,start,end):
            prefix = []
            ct = 0
            for j in text:
                if j == pattern[1]:
                    ct += 1
                prefix.append(ct)
            
            sub = 0
            for j in range(len(text)):
                if text[j] == pattern[0]:
                    sub += prefix[j]
            return start * end - sub
        
        d = {pattern[0] : 0,pattern[1] : 0}
        for i in text:
            d[i] = d.get(i,0) + 1
        start,end = d[pattern[0]],d[pattern[1]]
        
        if pattern[0] == pattern[1]:
            return start*(start+1) // 2
        if start <= end:
            return countSubs(pattern[0] + text,start+1,end)
        return countSubs(text + pattern[1],start,end+1)