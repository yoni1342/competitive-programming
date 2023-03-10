# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.inorder = []
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.rec(root)
        return self.inorder[k-1]
    
    def rec(self,curNode):
        if curNode:
            self.rec(curNode.left)
            self.inorder.append(curNode.val)
            self.rec(curNode.right)