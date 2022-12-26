class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        averag = 0
        sumation = 0
        n = len(salary)
        for i in range(0,len(salary)-1):
            if i != 0 and i != len(salary)-1:
                sumation = sumation + salary[i]
        
        averag = sumation / (n - 2) 
        return averag