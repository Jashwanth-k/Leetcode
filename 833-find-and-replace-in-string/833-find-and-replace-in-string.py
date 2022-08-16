class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        n = len(s)
        k = len(indices)
        helper = []
        for idx,src,tar in zip(indices,sources,targets):
            m = len(src)
            if s[idx:idx+m] == src:
                helper.append([idx,m,tar])
                
        helper.sort()
        res = []
        prev = 0
        for i in range(len(helper)):
            idx, src, tar = helper[i]
            if prev != idx:
                res.append(s[prev:idx])
            res.append(tar)
            prev = idx + src
        if prev <= n-1:
            res.append(s[prev:])
        return "".join(res)