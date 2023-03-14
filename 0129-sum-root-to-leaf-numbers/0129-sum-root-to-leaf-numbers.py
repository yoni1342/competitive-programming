# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root:
            self.DFS(root,str(0))
            # self.DFS(root.right,str(root.val))
        return self.ans
    def DFS(self,cur_node, digits):
        if not cur_node:
            return
        if not cur_node.left and not cur_node.right:
            self.ans+=int(digits+str(cur_node.val))
            return
        self.DFS(cur_node.left, digits+str(cur_node.val))
        self.DFS(cur_node.right, digits+str(cur_node.val))
        