class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        n = len(arr)
        d = collections.defaultdict(list)
        for i in range(n):
            d[arr[i]].append(i)

        res = [0] * n
        for i in d:
            sublist = d[i]
            rsum = sum(sublist)
            lsum = 0
            m = len(sublist)
            for i in range(m):
                curr = sublist[i]
                rsum -= curr
                res[curr] += abs(lsum - (i - 0) * curr)
                res[curr] += abs(rsum - (m - i - 1) * curr)
                lsum += curr
        return res