# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.find(root, subRoot)
        return self.ans
    
    def find(self, curr, sub):
        if not curr:
            return
        if curr.val == sub.val:
            if self.comp(curr, sub):
                self.ans = True
        self.find(curr.left, sub)
        self.find(curr.right, sub)
    def comp(self,p,q):
        if not p and not q:
            return True
        
        if not p or not q or p.val!=q.val:
            return False
        
        left = self.comp(p.left, q.left)
        right = self.comp(p.right, q.right)
        
        return left and right
    