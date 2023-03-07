# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root:
            self.depth(root)
            return self.max
    def depth(self, curNode):
        if not curNode:
            return 0
        
        left = self.depth(curNode.left)
        right = self.depth(curNode.right)
        self.max = max(self.max, left+right)
        return max(left,right)+1