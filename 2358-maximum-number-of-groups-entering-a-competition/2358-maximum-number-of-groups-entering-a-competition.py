class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        grades.sort()
        n = len(grades)
        length = 1
        i = 0
        while i < n:
            for k in range(i,i+length):
                if k >= n:
                    return length-1
            i += length
            length += 1
        return length-1