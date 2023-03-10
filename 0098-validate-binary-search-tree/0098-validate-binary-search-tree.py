# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.inorder = []
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.rec(root)
        i = 0
        while i < len(self.inorder)-1:
            if self.inorder[i]>=self.inorder[i+1]:
                return False
            i+=1
        return True
    def rec(self, curNode):
        if curNode:
            self.rec(curNode.left)
            self.inorder.append(curNode.val)
            self.rec(curNode.right)