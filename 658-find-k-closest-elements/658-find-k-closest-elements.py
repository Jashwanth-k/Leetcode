class Solution:
    def binarySearch(self,arr,target):
        s = 0
        e = len(arr) - 1
        while s <= e:
            mid = s + (e-s) // 2
            if arr[mid] == target:
                return mid,mid
            elif arr[mid] < target:
                s = mid + 1
            else:
                e = mid - 1
        if e < 0:
            return s, s
        if s >= len(arr):
            return e,e
        return s,e
        
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        mid = self.binarySearch(arr,x)
        if abs(arr[mid[0]] - x) < abs(arr[mid[1]] - x):
            idx = mid[0]
        else:
            idx = mid[1]
        output = []
        l = idx - 1
        r = idx + 1
        output.append(arr[idx])
        
        while len(output) < k:
            if r >= len(arr) or (l >= 0 and abs(arr[l] - x) <= abs(arr[r] - x)):
                output = [arr[l]] + output
                if len(output) == k:
                    break
                l -= 1
            elif r < len(arr):
                output.append(arr[r])
                r += 1

        return output
        