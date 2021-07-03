class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        x  = int(math.sqrt(area))
        
        while True:
            y = area/x
            if y.is_integer():
                if x > y:
                    return [x, int(y)]
                else:
                    return [int(y), x]
            x -= 1