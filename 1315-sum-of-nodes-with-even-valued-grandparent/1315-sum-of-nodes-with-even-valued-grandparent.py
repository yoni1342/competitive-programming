# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.dfs(root,-1,-1 )
        return self.ans
    
    def dfs(self, curNode, parent, gran):
        if not curNode:
            return
        if gran % 2 == 0:
            self.ans += curNode.val
        
        self.dfs(curNode.left, curNode.val, parent)        
        self.dfs(curNode.right, curNode.val, parent)