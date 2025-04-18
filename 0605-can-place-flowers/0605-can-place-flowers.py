class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        planted = 0
        for i in range(len(flowerbed)):
            can_left = (flowerbed[i-1] == 0 if i - 1 >= 0 else True)
            can_right = (flowerbed[i + 1] == 0 if i + 1 < len(flowerbed) else True)
            if can_left and can_right and flowerbed[i] == 0:
                planted += 1
                flowerbed[i] = 1
        return planted >= n