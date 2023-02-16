# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            self.DFS(root, 0)
            return self.max
        return 0
        
    def DFS(self, curNode, count):
        if not curNode:
            return
        count+=1
        self.max = max(self.max, count)
        self.DFS(curNode.left, count)
        count-=1
        count+=1
        self.max = max(self.max, count)
        self.DFS(curNode.right, count)
        count-=1