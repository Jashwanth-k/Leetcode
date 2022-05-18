class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        helper = []
        for i in timePoints:
            hrs = int(i[:2]) * 60
            minut = int(i[3:])
            total = hrs + minut
            helper.append(total)

        helper.sort()
        ans = 1440
        for i in range(1,len(helper)):
            curr = helper[i]
            left = helper[i-1]
            ans = min(ans,abs(left-curr))
        ans = min(ans,(1440-helper[-1]) + helper[0])
        return ans