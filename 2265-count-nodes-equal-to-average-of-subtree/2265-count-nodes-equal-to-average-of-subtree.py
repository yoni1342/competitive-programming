# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.rec(root)
        return self.ans
    def rec(self,node):
        if not node:
            return [0,0]
        
        left = self.rec(node.left)
        right = self.rec(node.right)
        
        total = node.val+left[0]+right[0]
        count = left[1]+right[1]+1
        
        avg = total//count
        if avg == node.val:
            self.ans+=1
            
        return [total, count]