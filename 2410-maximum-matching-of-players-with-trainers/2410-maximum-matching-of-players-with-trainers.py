class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        i = 0
        j = 0
        
        ans = 0
        
        while j<len(trainers) and i<len(players):
            while j<len(trainers) and players[i]>trainers[j]:
                j+=1
            
            if j<len(trainers) and players[i]<=trainers[j]:
                ans+=1
                i+=1
                j+=1
        return ans