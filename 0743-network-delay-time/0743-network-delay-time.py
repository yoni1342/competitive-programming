class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        
        def dijkstra(graph, start):
            distances = [float('inf')]*(n+1)
            
            distances[start] = 0
            visited = set()
            
            que = [(0, start)]
            
            while que:
                currCost, currNode = heapq.heappop(que)
                
                if currNode in visited:
                    continue
                
                for neighbor, weight in graph[currNode]:
                    distance = currCost + weight
                    
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(que, (distance, neighbor))
            
            return distances                        
        
        graph = defaultdict(list)
        
        for cur,nei,w in times:
            graph[cur].append([nei,w])
        
        distance = dijkstra(graph, k)
        
        return max(distance[1:]) if max(distance[1:]) != float('inf') else -1
        