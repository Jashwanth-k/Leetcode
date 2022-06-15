class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        def checkStr(s1,s2):
            for i in range(len(s1)):
                if s1[i] != s2[i] and s1[i] not in mapp[s2[i]]:
                    return False
            return True
        
        mapp = collections.defaultdict(set)
        for i,j in mappings:
            mapp[i].add(j)
        
        curr = collections.deque()
        sub = list(sub)
        i = 0
        for j in range(len(s)):
            curr.append(s[j])
            if (j-i+1) == len(sub):
                if checkStr(curr,sub):
                    return True
                curr.popleft()
                i += 1
        return False