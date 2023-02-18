# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.DFS(root)
        return root
    
    def DFS(self,curNode):
        if not curNode:
            return
        
        curNode.left, curNode.right = curNode.right, curNode.left
        self.DFS(curNode.left)
        self.DFS(curNode.right)