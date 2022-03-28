class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def reachHelper(arr, start, n, vl,vr):
            if arr[start] == 0:
                return True

            right = left = False
            rightind = start + arr[start]
            leftind = start - arr[start]
            if rightind < n and vr[rightind] == False:
                vr[rightind] = True
                right = reachHelper(arr, start + arr[start], n,vl,vr)
            if leftind >= 0 and vl[leftind] == False:
                vl[leftind] = True
                left = reachHelper(arr, start - arr[start], n,vl,vr)
            return right or left

        n = len(arr)
        vl = [False] * n
        vr = [False] * n
        return reachHelper(arr, start, n,vl,vr)