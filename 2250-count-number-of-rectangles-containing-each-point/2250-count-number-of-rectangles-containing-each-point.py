class Solution:
    def binarySearch(self,rectangles,si,ei,target):
        idx = 10**5
        while si <= ei:
            mid = si + (ei-si) // 2
            if target <= rectangles[mid]:
                idx = mid
                ei = mid - 1
            else:
                si = mid + 1
        if idx == 10**5:
            return si
        return idx
    
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        output = []
        hmap = defaultdict(list)
        for i,j in rectangles:
            hmap[j].append(i)
        for i,j in hmap.items():
            j.sort()
        
        for x, y in points:
            ct = 0
            for height in range(y,101):
                if height in hmap:
                    lengths = hmap[height]
                    n = len(lengths)
                    idx = self.binarySearch(lengths, 0, n - 1, x)
                    ct += n - idx
            output.append(ct)
        return output