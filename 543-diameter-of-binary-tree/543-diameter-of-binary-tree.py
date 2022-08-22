# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        memo = defaultdict(lambda: None)
        res = 0
        def depth(node):
            if node is None:
                return 0
            if memo[node] is not None:
                return memo[node]
            res = max(depth(node.left), depth(node.right)) + 1
            memo[node] = res
            return res
        
        def helper(node):
            nonlocal res
            if node is None:
                return
            res = max(res, depth(node.left) + depth(node.right)) 
            helper(node.left)
            helper(node.right)
        helper(root)
        return res
    