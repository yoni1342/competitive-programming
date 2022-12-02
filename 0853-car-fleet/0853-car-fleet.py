class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        Hash,stack, count = {}, [], 0
        for i in range(len(position)):
            Hash[position[i]] = speed[i]
        sortedHash = sorted(Hash.items(), key=lambda x: x[0], reverse=True)
        
        for i in sortedHash:
            time = (target-i[0])/i[1]
            
            if len(stack)==0 or stack[0]>= time:
                stack.append(time)
            elif stack[0]<time:
                stack.clear()
                count+=1
                stack.append(time)
        if len(stack)>0:
            count+=1
        return count