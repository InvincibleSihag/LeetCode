# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if node is None:
                return 0
            return max(helper(node.left)+1, helper(node.right)+1)
        return helper(root)
    