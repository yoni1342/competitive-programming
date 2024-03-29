# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = deque()
        q.append(root)
        right = True
        while q:
            qlen = len(q)
            level = []
            
            for i in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                if right:
                    ans.append(level)
                else:
                    ans.append(level[::-1])
            right = not right
            
        return ans
