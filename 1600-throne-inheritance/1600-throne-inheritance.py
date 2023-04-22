class ThroneInheritance:

    def __init__(self, kingName: str):
        self.graph = defaultdict(list)
        self.det = set()
        self.kingName = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)

    def death(self, name: str) -> None:
        self.det.add(name)

    def getInheritanceOrder(self) -> List[str]:
        
        def dfs(node, visited,ans):
            for i in self.graph[node]:
                if i not in visited:
                    if i not in self.det:
                        ans.append(i)
                    visited.add(i)  
                    dfs(i,visited,ans)
            return ans
        
        return dfs(self.kingName,set(),[] if self.kingName in self.det else [self.kingName])
    
            
                    


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()