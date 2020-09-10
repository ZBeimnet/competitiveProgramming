class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        plots = 0
        for i in range(len(flowerbed)):
            if not flowerbed[i]:
                if i == 0:
                    if len(flowerbed) > 1 and not flowerbed[i + 1]:
                        flowerbed[i] = 1
                        plots += 1
                    elif len(flowerbed) == 1:
                        plots += 1
                elif i == len(flowerbed) - 1 and not flowerbed[i - 1]:
                    plots += 1
                else:
                    if not flowerbed[i - 1] and not flowerbed[i + 1]:
                        flowerbed[i] = 1
                        plots += 1
        return plots >= n

