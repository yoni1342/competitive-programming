"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root:
            return self.dfs(root)
        return 0
    def dfs(self,node):
        if len(node.children) == 0:
            return 1
        
        neighbours = []
        
        for chiled in node.children:
            neighbours.append(self.dfs(chiled))
        
        return max(neighbours)+1