class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        minLocation = float('inf')
        dict = {}
        ans = -1
        for i in range(len(points)):
            if x == points[i][0]  or y == points[i][1]:
                distance = abs(x - points[i][0]) + abs(y - points[i][1])
                if distance < minLocation:
                    minLocation = distance
                    ans = i
        return ans
        
            
        
        
        