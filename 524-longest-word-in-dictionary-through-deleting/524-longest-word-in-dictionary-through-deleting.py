class Solution:
    def match(self,s,t,n,m):
        i = j = 0
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        return j == m
        
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        ans = ""
        length = 0
        n = len(s)
        for subs in dictionary:
            m = len(subs)
            if self.match(s,subs,n,m):
                if m > length:
                    ans = subs
                    length = m
                elif m == length:
                    ans = min(ans,subs)
        return ans