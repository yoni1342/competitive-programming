class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = str(root.val)
        if root.left:
            ans += '(' + self.tree2str(root.left) + ')'
        if root.right:
            if not root.left:
                ans += '()'
            ans+= '(' + self.tree2str(root.right) + ")"
        return ans