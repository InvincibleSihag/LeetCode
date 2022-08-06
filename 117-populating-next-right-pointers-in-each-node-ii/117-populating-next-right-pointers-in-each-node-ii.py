"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue = []
        if root is None:
            return root
        queue.append(root)
        
        while queue:
            
            size = len(queue)
            
            for i in range(size-1):
                queue[i].next = queue[i+1]
                if queue[i].left is not None:
                    queue.append(queue[i].left) 
                if queue[i].right is not None:    
                    queue.append(queue[i].right) 
            if queue[size-1].left is not None:
                queue.append(queue[size-1].left)
            if queue[size-1].right is not None:
                queue.append(queue[size-1].right)
            queue[size-1].next = None
            queue = queue[size:]
            # for val in queue:
            #     print(val.val, end='')
            # print('')
        return root
    