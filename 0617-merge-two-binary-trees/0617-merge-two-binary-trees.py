# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        return self.DFS(root1, root2)
        
        
    
    def DFS(self, root1, root2):
        
        if root1 and root2:
            
            root1.val += root2.val
            root1.left = self.DFS(root1.left, root2.left)
            root1.right = self.DFS(root1.right, root2.right)
            
            return root1
        
        else:
            
            return root1 or root2