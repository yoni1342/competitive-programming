class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        graph = defaultdict(list)

        if edges == []:
            return sum(price) // 2 
            
        def bfs(src, dest):

            queue = deque([(src, [src])])
            visited = set()
            visited.add(src)           

            while queue:
                node, path = queue.popleft()

                if node == dest:
                    return path

                for neighbour in graph[node]:
                    if neighbour not in visited:
                        queue.append([neighbour, path + [neighbour]])
                        visited.add(neighbour)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        freq = defaultdict(int)

        for src, dest in trips:
            path = bfs(src, dest)
            for node in path:
                freq[node] += 1

        @cache
        def dp(node, shouldHalf, parent):
            if shouldHalf:
                cost = freq[node] * ( price[node] // 2)
            else:
                cost = freq[node] * price[node]

            for neighbour in graph[node]:
                if neighbour != parent: 
                    if shouldHalf:
                        neiCost = dp(neighbour, False, node)
                    else:
                        neiCost = min(dp(neighbour, False, node), dp(neighbour, True, node))
                    cost += neiCost

            return cost

        cost = float("inf")
        for node in graph:
            cost = min(cost, dp(node, False, None), dp(node, True, None))

        return cost