class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        
        que = deque(rooms[0])
        
        while que:
            key = que.popleft()
            visited.add(key)
            
            for i in rooms[key]:
                if i not in visited:
                    que.append(i)
        
        return len(visited) == len(rooms)