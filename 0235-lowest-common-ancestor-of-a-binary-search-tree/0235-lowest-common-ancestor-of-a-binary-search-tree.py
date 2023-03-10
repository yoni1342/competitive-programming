# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.rec(root,p,q)
    def rec(self, curNode,p,q):
        if not curNode:
            return
        if p.val <= curNode.val <= q.val:
            return curNode
        if p.val >= curNode.val >= q.val:
            return curNode
        
        if p.val < curNode.val:
            return self.rec(curNode.left,p,q)
        else:
            return self.rec(curNode.right,p,q)