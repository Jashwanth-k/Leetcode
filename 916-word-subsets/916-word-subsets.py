class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        freq = defaultdict(int)
        for s in words2:
            d = Counter(s)
            for i in d:
                freq[i] = max(freq[i],d[i])
        
        res = []
        for s in words1:
            curr = Counter(s)
            if all(freq[i] <= curr[i] for i in freq):
                res.append(s)
        return res