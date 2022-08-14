# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import defaultdict
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = defaultdict(lambda: None)
        def helper(node):
            if node is None:
                return 0
            if memo[node] != None:
                return memo[node]
            res1 = node.val + sum([helper(None if nextNode is None else nextNode.left) +
                               helper(None if nextNode is None else nextNode.right) for nextNode in [node.left, node.right]])
            res2 = helper(node.left) + helper(node.right)
            memo[node] = max(res1, res2)
            return memo[node]
        
        return helper(root)