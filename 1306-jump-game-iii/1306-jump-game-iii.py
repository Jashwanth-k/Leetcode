class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def reachHelper(arr, start, n):
            if start < 0 or start >= n or arr[start] < 0:
                return False
            if arr[start] == 0:
                return True

            val = arr[start]
            arr[start] = -arr[start]
            right = reachHelper(arr, start + val, n)
            left = reachHelper(arr, start - val, n)
            return right or left

        n = len(arr)
        return reachHelper(arr, start, n)