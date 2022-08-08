# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        output = []

        def helper(node, target, path):
            if node is None:
                return
            if node.left is None and node.right is None and target-node.val == 0:
                path.append(node.val)
                output.append(list(path))
                path.pop()
                return
            path.append(node.val)
            helper(node.left, target-node.val, path)
            helper(node.right, target-node.val, path)
            path.pop()
        
        helper(root, targetSum, [])
        return output
    