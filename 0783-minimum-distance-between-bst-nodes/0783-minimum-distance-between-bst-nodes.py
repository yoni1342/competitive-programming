# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.minDistance = float('inf')
        self.prev = None
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.DFS(root)
        return self.minDistance
    
    def DFS(self, curNode):
        if not curNode:
            return
        self.DFS(curNode.left)
        
        if self.prev:
            self.minDistance = min(self.minDistance, abs(curNode.val-self.prev.val))
        self.prev = curNode
        
        self.DFS(curNode.right)
        
        return curNode.val