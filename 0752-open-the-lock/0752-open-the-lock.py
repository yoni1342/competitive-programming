class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        visited = set(deadends)
        que = deque([("0000",0)]) if "0000" not in visited else []
        
        
        while que:
            
            for i in range(len(que)):
                pattern,level = que.popleft()
                
                if pattern == target:
                    return level
                
                for i in range(len(pattern)):
                    if pattern[i] == "9":
                        new = pattern[:i]+"0"+pattern[i+1:]
                    else:
                        new = pattern[:i]+str(int(pattern[i])+1)+pattern[i+1:]
                    if new not in visited:
                        que.append((new, level+1))
                        visited.add(new)
                    
                    if pattern[i] == "0":
                        new = pattern[:i]+"9"+pattern[i+1:]
                    else:
                        new = pattern[:i]+str(int(pattern[i])-1)+pattern[i+1:]
                    
                    if new not in visited:
                        que.append((new, level+1))
                        visited.add(new)
        return -1