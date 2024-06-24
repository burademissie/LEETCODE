class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        num = 0
        players.sort()
        trainers.sort()
        for i in range(len(trainers)):
            if players[num]<=trainers[i] :
                num += 1
                if len(players) == num:
                    return num
        return num

        
