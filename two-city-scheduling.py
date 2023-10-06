class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []
        
        for a,b in costs:
            diff.append([a-b,[a,b]])
        diff.sort()
        l = 0
        r = len(diff)-1
        summ = 0
       
        while l < r:
            summ += diff[l][1][0]
            l += 1
            summ += diff[r][1][1]
            r -= 1
        
        return summ