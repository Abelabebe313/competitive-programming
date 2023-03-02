class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[2],reverse=True)
        maximum = trips[0][2]
        lineSweep = [0] * (maximum + 1)
        
        for passengers, start, end in trips:
            lineSweep[start] += passengers
            lineSweep[end] -= passengers
        total = 0
        for num in lineSweep:
            total += num
            if total > capacity:
                return False
        return True