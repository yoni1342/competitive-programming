class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        tickets[k] = [tickets[k],k]
        queue = deque(tickets)
        res = 0
        
        while True:
            
            val = queue.popleft()
            
            if isinstance(val,list):
                if val[0] == 1:
                    res += 1
                    break
                    
                else:
                    val[0] -= 1
                    res += 1
                    queue.append(val)
                    
                    
            else:
                res += 1
                val -= 1
                
                if val > 0:
                    queue.append(val)
        
        return res