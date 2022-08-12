# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def helper(node):
            if node is None:
                return None
            if node.val == p.val or node.val == q.val:
                return node 
            left = helper(node.left)
            right = helper(node.right)
            
            if left is not None and right is not None:
                return node
            
            return left if left is not None else right
        
        return helper(root)
    