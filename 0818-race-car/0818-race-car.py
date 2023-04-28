class Solution:
    def racecar(self, target: int) -> int:
        que = deque([(0,1,0)])
        visited = set([(0,1)])
        
        while que:
            
            for i in range(len(que)):
                
                pos, speed, level = que.popleft()
                
                if pos == target:
                    return level
                
                # accelerate
                if (pos+speed, speed*2) not in visited:
                    visited.add((pos+speed, speed*2))
                    que.append(((pos+speed, speed*2, level+1)))
                
                # reverese
                if speed > 0:
                    if (pos, -1) not in visited:
                        visited.add((pos, -1))
                        que.append((pos, -1, level+1))
                else:
                    if (pos, 1) not in visited:
                        visited.add((pos, 1))
                        que.append((pos,1,level+1))