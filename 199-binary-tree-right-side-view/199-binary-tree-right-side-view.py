# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        output = []
        if root is not None:
            queue.append(root)
        
        while queue:
            size = len(queue)
            output.append(queue[0].val)
            for _ in range(size):
                node = queue.popleft()
                if node.right is not None:
                    queue.append(node.right)
                if node.left is not None:
                    queue.append(node.left)
            # queue = queue[size:]
        return output
        