class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indegree = defaultdict(int)
        outdegree = defaultdict(list)
        ans = []
        queue = deque()
        check = set(recipes)

        for elm in supplies:
            queue.append(elm)
        
        for idx, recipe in enumerate(recipes):
            indegree[recipe] = len(ingredients[idx])

            for elm in ingredients[idx]:
                outdegree[elm].append(recipe)
        
        while queue:
            cur = queue.popleft()
            if cur in check:
                ans.append(cur)
            
            for elm in outdegree[cur]:
                indegree[elm] -= 1

                if indegree[elm] == 0:
                    queue.append(elm)

        return ans