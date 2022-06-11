class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        res = [0,0]
        flowerbed = [0] + flowerbed + [0]
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i] != 1 and (flowerbed[i-1] == 0 and flowerbed[i+1] == 0):
                res[i%2] += 1
        return max(res) >= n