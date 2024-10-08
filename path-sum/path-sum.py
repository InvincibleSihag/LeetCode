# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        def helper(node, target):
            if node is None:
                return False
            if node.left is None and node.right is None and target-node.val == 0:
                return True
            return helper(node.left, target-node.val) or helper(node.right, target-node.val)
        
        return helper(root, targetSum)
    