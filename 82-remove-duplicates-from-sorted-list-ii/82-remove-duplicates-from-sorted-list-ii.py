# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = newHead = ListNode()
        temp.next = head
        while temp.next is not None:
            cur = temp.next
            count = 0
            while cur is not None and cur.val == temp.next.val:
                cur = cur.next
                count += 1
            if count > 1:
                temp.next = cur
            else:
                temp = temp.next
        return newHead.next
    