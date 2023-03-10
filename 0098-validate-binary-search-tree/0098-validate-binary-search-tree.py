# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.temp = float("-inf")
        self.ans = True
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.rec(root)
        return self.ans
    def rec(self, curNode):
        if curNode:
            self.rec(curNode.left)
            if self.temp >= curNode.val:
                self.ans = False
                return
            self.temp = curNode.val
            self.rec(curNode.right)