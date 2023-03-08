# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.rec(root.left, root.right)
    
    def rec(self, leftNode, rightNode):
        if not rightNode and not leftNode:
            return True
        
        if not leftNode or not rightNode or rightNode.val!=leftNode.val:
            return False
        
        left  = self.rec(leftNode.left, rightNode.right)
        right = self.rec(leftNode.right,rightNode.left)
        
        return left and right