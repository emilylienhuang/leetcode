class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            left = flowerbed[i - 1] == 0 if i - 1 >= 0 else True
            right = flowerbed[i + 1] == 0 if i + 1 < len(flowerbed) else True
            if left and right and flowerbed[i] != 1:
                flowerbed[i] = 1
                count += 1
        return (count >= n)