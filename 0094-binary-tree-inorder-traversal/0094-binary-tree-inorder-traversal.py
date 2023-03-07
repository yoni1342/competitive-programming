# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            self.dfs(root)
        return self.ans
    
    def dfs(self,cur_node):
        if cur_node:
            self.dfs(cur_node.left)
            self.ans.append(cur_node.val)
            self.dfs(cur_node.right)