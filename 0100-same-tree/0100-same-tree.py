# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.rec(p,q)
    def rec(self,p,q):
        if not p and not q:
            return True
        
        if not p or not q or p.val!=q.val:
            return False
        
        left = self.rec(p.left, q.left)
        right = self.rec(p.right, q.right)
        
        return left and right