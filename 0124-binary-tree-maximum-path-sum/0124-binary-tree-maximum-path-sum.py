class Solution:
    def __init__(self):
        self.ans = float('-inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.DFS(root)
        return self.ans 
    def DFS(self, cur_node):
        if not cur_node:
            return float('-inf')
        self.ans = max(self.ans, cur_node.val)
        if not cur_node.left and not cur_node.right:
            return cur_node.val
        Left = self.DFS(cur_node.left)
        Left = 0 if Left == float('-inf') else Left
        Right = self.DFS(cur_node.right)
        Right = 0 if Right == float('-inf') else Right
        self.ans = max(self.ans, max(Left,Right)+cur_node.val)
        self.ans = max(self.ans, (cur_node.val+Right+Left))

        if cur_node.val+max(Left,Right)<cur_node.val:
            return cur_node.val
        return cur_node.val+max(Left,Right)
         