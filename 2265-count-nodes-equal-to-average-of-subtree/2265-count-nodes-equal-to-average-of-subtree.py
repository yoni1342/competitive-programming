# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        return self.rec(root)[2]
    def rec(self,node):
        if not node:
            return [0,0,0]
        
        left = self.rec(node.left)
        right = self.rec(node.right)
        
        total = node.val+left[0]+right[0]
        count = left[1]+right[1]+1
        ans = left[2]+right[2]
        
        avg = total//count
        if avg == node.val:
            ans+=1    
            
        return [total, count, ans]