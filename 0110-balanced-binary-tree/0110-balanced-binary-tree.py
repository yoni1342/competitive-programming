# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root:
            self.rec(root)
            return self.ans
        else:
            return True
    def rec(self,curNode):
        if not curNode:
            return 0
        
        left = self.rec(curNode.left)
        right = self.rec(curNode.right)
        
        if abs(right-left)>1:
            self.ans = False
        
        return max(right, left)+1
            