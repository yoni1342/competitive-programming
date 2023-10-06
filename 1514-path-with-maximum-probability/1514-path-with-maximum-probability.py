class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        def dijkstra(graph, start):
            probabilities = [float(-inf)]*n
            probabilities[start] = 0
            visited = set()
            
            heap = [(1, start)]
        
            while heap:
                curprob, currnode = heapq.heappop(heap)
                if currnode not in visited:
                    visited.add(currnode)
                    
                    for neighbor, probability in graph[currnode]:
                        prob = abs(curprob)*probability
                        
                        if prob > probabilities[neighbor]:
                            probabilities[neighbor] = prob
                            heapq.heappush(heap, (-prob, neighbor))
            
            return probabilities[end_node]
        
        
        
        graph = defaultdict(list)
        
        for idx,edge in enumerate(edges):
            i, j = edge
            graph[i].append((j, succProb[idx]))            
            graph[j].append((i, succProb[idx]))
        
        # print(graph)
        res = dijkstra(graph, start_node)
        return 0 if res == float("-inf") else res