class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0,1)])
        visited = set([(0,1)])
        path = 0
        
        while queue:
            for i in range(len(queue)):
                pos,speed = queue.popleft()
                if pos == target:
                    return path
                
                for instruct in ['A','R']:
                    if instruct == 'A':
                        if(pos+speed,speed*2) not in visited:
                            queue.append((pos+speed,speed*2))
                            visited.add((pos+speed,speed*2))
                    elif instruct == 'R':
                        if speed > 0 and (pos,-1) not in visited:
                            queue.append((pos,-1))
                            visited.add((pos,-1))
                        elif speed <= 0 and (pos,1) not in visited:
                            queue.append((pos,1))
                            visited.add((pos,1))
           
            path += 1
        return -1