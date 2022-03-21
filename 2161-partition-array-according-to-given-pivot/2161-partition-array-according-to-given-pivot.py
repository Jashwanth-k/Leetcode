class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        output = []
        for i in nums:
            if i == pivot:
                output.append(i)
        midst = 0

        for i in nums:
            if i < pivot:
                output.insert(midst,i)
                midst += 1
            elif i > pivot:
                output.append(i)
        return output