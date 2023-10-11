# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count, sum_ = 0, 0
        hash_map = defaultdict(int)
        hash_map[0] = 1
        
        def helper(cur, r_sum):
            nonlocal count
            if not cur:
                return
            r_sum += cur.val
            
            # if r_sum - targetSum in hash_map:
            count += hash_map[r_sum - targetSum]
            hash_map[r_sum] += 1
            
            helper(cur.left, r_sum)
            helper(cur.right, r_sum )
            hash_map[r_sum] -= 1
        
        helper(root, sum_)
        
        return count