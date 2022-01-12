class Solution:
    def binarySearch(self,s,e,arr,target):
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
        mid = self.binarySearch(0,len(arr)-1,arr,x)
        if abs(arr[mid[0]] - x) < abs(arr[mid[1]] - x):
            idx = mid[0]
        else:
            idx = mid[1]
        output = [arr[idx]]
        l = idx - 1
        r = idx + 1
        
        while len(output) < k:
            if r >= len(arr) or (abs(arr[l] - x) <= abs(arr[r] - x)):
                output = [arr[l]] + output
                if len(output) == k:
                    break
                l -= 1
            else:
                output.append(arr[r])
                r += 1
        return output
        