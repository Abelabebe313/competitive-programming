class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        goodmeal = 0
        meals = {}
        modulo = ((10**9) + 7)
        
        for i in deliciousness:
            for j in range(22):
                power = (2**j) - i
                
                if power in meals:
                    goodmeal += meals[power]
                    
            if not i in meals:
                meals[i] = 0
            meals[i] += 1
        
        return goodmeal % modulo