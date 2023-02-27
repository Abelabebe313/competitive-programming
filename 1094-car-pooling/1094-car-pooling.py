class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        lst = []
        current = 0
        for ppl, strt,end in trips:
            lst.append((strt,ppl,1))
            lst.append((end,ppl,0))
        
        lst.sort(key = lambda x: (x[0],x[2]))
        
        for time,people,pickup in lst:
            if pickup:
                current += people
            else:
                current -= people
            if current > capacity:
                return False
        return True