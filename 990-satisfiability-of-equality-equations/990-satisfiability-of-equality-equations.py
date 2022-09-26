class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def DFS(si,pair):
            visited[ord(si) - 97] = True
            pair.add(si)
            for sib in d[si]:
                if visited[ord(sib) - 97] == False:
                    DFS(sib,pair)
            
        d = defaultdict(list)
        for s in equations:
            if s[1] == "!": continue
            d[s[0]].append(s[3])
            d[s[3]].append(s[0])
            
        pairsets = []
        visited = [False]*26
        for i in range(25):
            if visited[i] == False:
                pair = set()
                DFS(chr(i + 97),pair)
                pairsets.append(pair)
        for s in equations:
            if s[1] == "!":
                for pairs in pairsets:
                    if s[0] in pairs and s[3] in pairs:
                        return False
        return True