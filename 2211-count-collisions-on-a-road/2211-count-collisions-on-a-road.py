class Solution:
    def countCollisions(self, directions: str) -> int:
        prev,res,prer = "",0,0
        collide = False
        for curr in directions:
            if prev == "S":
                if curr == "L":
                    res += 1
                    collide = True
            elif prev == "R":
                if curr == "S":
                    res += prer
                    prer = 0
                    collide = True
                elif curr == "L":
                    res += 2 + prer-1
                    prer = 0
                    collide = True
            if collide:
                prev = "S"
                prevr = 0
                collide = False
            else:
                prev = curr
                if curr == "R": prer += 1
        return res