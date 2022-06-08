class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i,letter in enumerate(s):
            d[letter] = i
        
        ans = []
        start = end = 0
        for i,letter in enumerate(s):
            end = max(end,d[letter])
            if i == end:
                ans.append(end-start+1)
                start = end+1
        return ans