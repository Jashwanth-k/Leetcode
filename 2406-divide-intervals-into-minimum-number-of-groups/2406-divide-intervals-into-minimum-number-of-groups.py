from sortedcontainers import SortedDict
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        ranges = SortedDict()
        for left,right in intervals:
            ranges[left] = ranges.get(left,0) + 1
            ranges[right+1] = ranges.get(right+1,0) - 1
            
        res = 1
        curr = 0
        for i in ranges:
            curr += ranges[i]
            res = max(res,curr)
        return res