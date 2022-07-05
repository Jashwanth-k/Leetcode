class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def binarySearch(target):
            si,ei = 0,m-1
            while si <= ei:
                mid = si + (ei-si) // 2
                if potions[mid] >= target:
                    ei = mid-1
                else:
                    si = mid+ 1
            return si
        
        n,m = len(spells),len(potions)
        potions.sort()
        output = []
        for i in spells:
            target = math.ceil(success / i) if success > i else 1
            currans = binarySearch(target)
            output.append(m - currans)
        return output