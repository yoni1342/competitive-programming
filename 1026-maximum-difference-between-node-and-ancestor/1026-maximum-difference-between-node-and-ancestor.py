# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def dfs(curNode, _min, _max):
            nonlocal ans
            
            if not curNode:
                ans = max(ans, abs(_min - _max))
                return
            
            _min = min(_min, curNode.val)            
            _max = max(_max, curNode.val)
            
            dfs(curNode.left, _min, _max)            
            dfs(curNode.right, _min, _max)
        
        dfs(root, root.val, root.val)
        return ans