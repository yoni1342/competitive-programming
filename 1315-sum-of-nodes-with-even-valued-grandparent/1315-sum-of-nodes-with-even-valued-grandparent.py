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
        self.dfs(root)
        return self.ans
    
    def dfs(self, curNode):
        if not curNode:
            return 
        
        if curNode.val % 2 == 0:
            if curNode.left:
                self.Sum(curNode.left)
            if curNode.right:
                self.Sum(curNode.right)
        
        self.dfs(curNode.left)
        self.dfs(curNode.right)
            
    def Sum (self, node):
        if node.left:
            self.ans += node.left.val
        if node.right:
            self.ans += node.right.val