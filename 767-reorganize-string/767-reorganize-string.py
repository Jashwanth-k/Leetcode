class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        freq = collections.defaultdict(int)
        for i in s: freq[i] += 1
        maxHp = []
        for i,j in freq.items():
            maxHp.append([-j,i])
        heapq.heapify(maxHp)
        
        ans = "#"
        while maxHp:
            curr, s1 = heapq.heappop(maxHp)
            if s1 == ans[-1]:
                if not maxHp: return ""
                curr2, s2 = heapq.heappop(maxHp)
                ans += s2
                if curr2 + 1 != 0:
                    heapq.heappush(maxHp,[curr2 + 1, s2])
                heapq.heappush(maxHp,[curr, s1])
            else:
                ans += s1
                if curr + 1 != 0:
                    heapq.heappush(maxHp,[curr + 1, s1])
        return ans[1:]