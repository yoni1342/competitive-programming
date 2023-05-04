class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        rq = deque()
        dq = deque()
        
        for i in range(len(senate)):
            if senate[i] == "R":
                rq.append(i)
            else:
                dq.append(i)
        
        while rq and dq:
            r = rq.popleft()
            d = dq.popleft()
            
            if r < d:
                rq.append(r+len(senate))
            else:
                dq.append(d+len(senate))
        
        return 'Radiant' if rq else 'Dire'