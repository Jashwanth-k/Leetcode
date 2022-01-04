class Solution:
    def binarySearch(self,nums,target,si,ei):
        idx = 0
        while si <= ei:
            mid = si + (ei-si) // 2
            if nums[mid] >= target:
                idx = mid
                
            if target <= nums[mid]:
                si = mid + 1
            else:
                ei = mid - 1
        return idx
        
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        maxim = 0
        for i in range(len(nums1)):
            j = self.binarySearch(nums2,nums1[i],i,len(nums2)-1)
            maxim = max(maxim,j-i)
        return maxim