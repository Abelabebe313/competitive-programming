class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque(rooms[0])
        
        key = set()
        key.add(0)
        
        while queue:
            temp = queue.popleft()
            key.add(temp)
            
            for i in rooms[temp]:
                if i not in key:
                    queue.append(i)
                
                
        if len(key) == len(rooms):
            return True
        return False
            