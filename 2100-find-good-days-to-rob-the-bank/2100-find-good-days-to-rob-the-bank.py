class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        def slidingWindow(si, ei, inc, flag):
            store = set()
            i = si
            curr = collections.deque()
            for j in range(si, ei, inc):
                while len(curr) != 0 and curr[-1] < security[j]:
                    curr.popleft()
                curr.append(security[j])
                if abs(j - i) + 1 == time:
                    if len(curr) == time:
                        if flag:
                            store.add((i,j))
                        else:
                            store.add((j,i))
                        curr.popleft()
                    i = i + 1 if flag else i - 1
            return store

        n = len(security)
        if time == 0: return [i for i in range(n)]
        decrease = slidingWindow(0, n, 1, True)
        increase = slidingWindow(n - 1, -1, -1, False)

        ans = []
        for i in range(time,n-time):
            if security[i-1] >= security[i] <= security[i+1]:
                if (i-time,i-1) in decrease and (i+1,i+time) in increase:
                    ans.append(i)
        return ans