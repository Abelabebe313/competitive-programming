from collections import Counter
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winnerDict = {}
        answer = []
        winner = []
        loser = []
        for i in range(len(matches)):
            if matches[i][0] not in winnerDict:
                winnerDict[matches[i][0]] = 0
                
            if matches[i][1] not in winnerDict:
                winnerDict[matches[i][1]] = 1
            elif matches[i][1] in winnerDict:
                winnerDict[matches[i][1]] += 1
                
        for key in winnerDict:
            if winnerDict[key] == 0:
                winner.append(key)
            elif winnerDict[key] ==  1:
                loser.append(key)
        winner.sort()
        loser.sort()
        answer.append(winner)
        answer.append(loser)
                
        
        
        return answer
            