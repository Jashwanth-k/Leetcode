class Solution:
    def binarySearch(self,arr,target):
        si,ei = 0,len(arr)-1
        while si <= ei:
            mid = si + (ei-si) // 2
            if arr[mid] == target:
                return mid
            elif target > arr[mid]:
                si = mid + 1
            else:
                ei = mid - 1
        return si
        
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [nums[0]]
        for el in nums:
            idx = self.binarySearch(arr,el)
            if idx == len(arr):
                arr.append(el)
            else:
                arr[idx] = el
        return len(arr)