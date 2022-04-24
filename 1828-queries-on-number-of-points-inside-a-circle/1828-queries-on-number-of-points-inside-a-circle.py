class Solution:
    def findPoints(self,points,h,k,r):
        ct = 0
        for x,y in points:
            if (x-h)**2 + (y-k)**2 <= r**2:
                ct += 1
        return ct
    
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        output = []
        for i,j,k in queries:
            ans = self.findPoints(points,i,j,k)
            output.append(ans)
        return output