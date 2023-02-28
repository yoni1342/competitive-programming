class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefix = [0]*1001
        
        for i in range(len(trips)):
            numPassi, fromi, toi = trips[i]
            
            prefix[fromi]+=numPassi
            prefix[toi]-=numPassi
        
        Max = max(list(accumulate(prefix)))
        
        return Max <= capacity