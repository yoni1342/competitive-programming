# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)
        
        
        def treeToGraph(curNode):
            if not curNode:
                return
            
            left = curNode.left
            right = curNode.right
            
            if left:
                graph[curNode.val].append(left.val)
                graph[left.val].append(curNode.val)
                treeToGraph(left)
            if right:
                graph[curNode.val].append(right.val)
                graph[right.val].append(curNode.val)
                treeToGraph(right)
        
        
        treeToGraph(root)
        
        ans = 0
        que = deque()
        visited = set()
        que.append((start,0))
        
        while que:
            cur,count = que.popleft()
            
            if cur not in visited:
                visited.add(cur)
                for neighbor in graph[cur]:
                    que.append((neighbor, count+1))
                    ans = max(ans, count)
        
        return ans
            
            