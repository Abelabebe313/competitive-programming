class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        pilesQue = collections.deque(piles)
        
        count = 0
        
        while len(pilesQue) > 0:
            pilesQue.popleft()
            pilesQue.pop()
            count += pilesQue[-1]
            pilesQue.pop()
        
        return count