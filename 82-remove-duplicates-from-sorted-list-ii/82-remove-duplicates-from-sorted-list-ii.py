# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = newHead = ListNode()
        temp.next = head
        first = True
        while temp.next is not None:
            cur = temp.next
            count = 0
            while cur is not None and cur.val == temp.next.val:
                cur = cur.next
                count += 1
            if count > 1:
                # if first:
                #     temp = newHead = ListNode()
                temp.next = cur
            else:
                temp = temp.next
                first = False
        return newHead.next
    