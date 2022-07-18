# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    # def helper(self, node):
    #     if node is None:
    #         return True
    #     if (node.left is not None and node.left.val >= node.val) or (node.right is not None and node.right.val <= node.val):
    #         return False
    #     return self.helper(node.left) and self.helper(node.right)
    
    def in_order(self, node):
        if node is None:
            return
        self.in_order(node.left)
        if self.prev_val is not None:
            if self.prev_val >= node.val:
                self.out = False
                return False
            else:
                self.prev_val = node.val
        else:
            self.prev_val = node.val
        self.in_order(node.right)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.in_order(root)
        return self.out
        
    def __init__(self):
        self.out = True
        self.prev_val = None
    