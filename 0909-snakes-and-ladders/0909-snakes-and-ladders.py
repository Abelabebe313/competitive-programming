class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)
        cordinate = defaultdict(list)
        curr = defaultdict(int)
        count = N*N
        spin = True if N%2==0 else False 
        for i in range(N):
            if spin:
                for j in range(N):
                    cordinate[count].append(i)
                    cordinate[count].append(j)
                    curr[(i,j)] = count
                    count -= 1
            else:
                for j in range(N-1,-1,-1):
                    cordinate[count].append(i)
                    cordinate[count].append(j)
                    curr[(i,j)] = count
                    count -= 1
            spin = not spin
        
        queue = deque()
        visited =set()
        queue.append([N-1,0,0])
        
        while queue:
            r,c,path = queue.popleft()
            currNum = curr[(r,c)]
            ran = [currNum+1,(min(currNum+6,N*N))+1]
            for i in range(ran[0],ran[1]):
                nr,nc = cordinate[i]
                if board[nr][nc] != -1:
                    cr,cc = cordinate[board[nr][nc]]
                    nr,nc = cr,cc
                if curr[(nr,nc)] == N * N:
                    return path + 1
                if (nr,nc) not in visited:
                    visited.add((nr,nc))
                    queue.append([nr,nc,path + 1])
                        
        return -1