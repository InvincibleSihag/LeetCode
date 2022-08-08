# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def helper(left, right):
            if left is not None and right is not None:
                if left.val != right.val:
                    return False
                else:
                    return helper(left.left, right.right) and helper(left.right, right.left)
            return left == right
        
        return helper(root.left, root.right)