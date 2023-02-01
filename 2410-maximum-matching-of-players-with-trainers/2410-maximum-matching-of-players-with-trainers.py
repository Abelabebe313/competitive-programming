class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        p1 = 0
        p2 = 0
        output = 0
        players.sort()
        trainers.sort()
        while p1 < len(players) and p2 < len(trainers):
            if p1 < len(players) and p2 < len(trainers):
                if players[p1] <= trainers[p2]:
                    output += 1
                    p1 += 1
                    p2 += 1
                elif players[p1] > trainers[p2]:
                    p2 += 1
        return output
                