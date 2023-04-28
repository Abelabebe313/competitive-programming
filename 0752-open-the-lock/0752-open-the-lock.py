class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque(['0000']) if '0000' not in deadends else deque()
        path = 0
        forbidden = set(deadends)
        visited = set(['0000'])
        
        
        while queue:
            length = len(queue)
            path += 1            
            for i in range(length):
                temp = queue.popleft()
                if temp == target:
                    return path - 1
                for j in range(4):
                    for delta in (-1,1):
                        new_digit = str((int(temp[j]) + delta) % 10)
                        
                        tem = temp[:j] + new_digit + temp[j+1:]
                        
                        if tem not in visited and tem not in forbidden:
                            queue.append(tem)
                            visited.add(tem)
        return -1
                    
        