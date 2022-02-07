class Solution:
    def linearSearch(self,nums2,si,ei,ele):
        for i in range(si,ei):
            if nums2[i] > ele:
                return nums2[i]
        return -1
        
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n,m = len(nums1),len(nums2)
        d = collections.defaultdict(None)
        for i,j in enumerate(nums2):
            d[j] = i
        
        output = [-1] * n
        for i in range(n):
            nbr = nums1[i]
            output[i] = self.linearSearch(nums2,d[nbr]+1,m,nbr)
        return output