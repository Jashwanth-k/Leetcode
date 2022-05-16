class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        i = j = 0
        n,m = len(nums1),len(nums2)
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
            
        nums += nums1[i:]
        nums += nums2[j:]
        n += m
        mid = (n-1) // 2
        if n % 2 == 0:
            return (nums[mid] + nums[mid+1]) / 2
        return nums[mid]