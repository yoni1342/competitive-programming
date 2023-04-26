# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        que = deque()
        que.append(root)
        
        while que:
            
            level = []
            for i in range(len(que)):
                node = que.popleft()
                
                if node:
                    level.append(node.val)
                    que.append(node.right)                    
                    que.append(node.left)
            
            if level:
                ans.append((sum(level) / len(level)))
        
        return ans