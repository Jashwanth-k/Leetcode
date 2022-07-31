class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        si,ei = 0,n
        while si <= ei:
            mid = si + (ei - si) // 2
            curlen = mid * (mid+1) // 2
            if curlen == n:
                return mid
            if curlen > n:
                ei = mid-1
            else:
                si = mid+1
        return ei