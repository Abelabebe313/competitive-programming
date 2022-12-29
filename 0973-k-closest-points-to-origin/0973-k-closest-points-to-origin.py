class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = sorted(points, key = lambda val: (val[0]**2 + val[1]**2))
        
        answer = []
        for index in range(k):
            answer.append(points[index])
        
        return answer 
        