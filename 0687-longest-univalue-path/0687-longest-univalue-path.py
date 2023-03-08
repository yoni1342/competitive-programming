# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if root:
            self.rec(root, root.val)
        return self.ans
    def rec(self, curNode, parent):
        if not curNode:
            return 0
        left = self.rec(curNode.left, curNode.val)
        right = self.rec(curNode.right, curNode.val)
        
        self.ans = max(self.ans, left+right)
        
        return 1+max(left, right) if curNode.val == parent else 0