# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def depth(node):
            if node is None:
                return 0
            return max(depth(node.left), depth(node.right)) + 1
        
        def helper(node):
            nonlocal res
            if node is None:
                return
            res = max(res, depth(node.left) + depth(node.right)) 
            helper(node.left)
            helper(node.right)
        helper(root)
        return res
    