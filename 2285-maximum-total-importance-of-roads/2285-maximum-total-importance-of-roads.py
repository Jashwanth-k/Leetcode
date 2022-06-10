class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        d = collections.defaultdict(int)
        for i,j in roads:
            d[i] += 1
            d[j] += 1
    
        count = collections.defaultdict(list)
        for i,j in d.items():
            count[j] += [i]
        
        for freq in range(n,-1,-1):
            sublist = count[freq]
            for j in sublist:
                d[j] = n
                n -= 1
                if n == 0:
                    break
        ans = 0
        for i,j in roads:
            ans += d[i] + d[j]
        return ans