class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        helper = [a,b,c]
        helper.sort()
        a,b,c = helper
        ans = [0,0]
        if b-a == 1 and c-b == 1:
            return [0,0]
        elif b-a <= 2 or c-b <= 2:
            ans[0] = 1
        else:
            ans[0] = 2
        ans[1] = (b-a-1) + (c-b-1)
        return ans