class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = len(trips)
        cnt = [0]*(1001)
        for passen,frm,to in trips:
            cnt[frm] += passen
            cnt[to] -= passen
        for i in range(1001):
            cnt[i] += cnt[i-1]
            if cnt[i] > capacity:
                return False
        return True