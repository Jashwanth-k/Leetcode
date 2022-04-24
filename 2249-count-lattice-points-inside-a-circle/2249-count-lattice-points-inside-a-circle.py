class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        def circlePaths(circles, hmap, h, k, r):
            xleft = h - r
            xright = h + r
            ytop = k + r
            ybottom = k - r

            for i in range(xleft,xright+1):
                for j in range(ybottom,ytop+1):
                    if (i,j) not in hmap:
                        if (i-h)**2 + (j-k)**2 <= r**2:
                            hmap[i,j] = True

        hmap = {}
        for i, j, k in circles:
            circlePaths(circles, hmap, i, j, k)
        return len(hmap)