# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def add_pending(self, li, carry, output, tail):
        while li != None:
            each_sum = li.val + carry
            if output.val == None:
                output.val = each_sum%10
                tail = output_list
            else:
                new_node = ListNode(val=each_sum%10)
                tail.next = new_node
                tail = tail.next
            carry = int(each_sum/10)
            li = li.next
        if carry != 0:
            new_node = ListNode(val=carry)
            tail.next = new_node
            tail = tail.next
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output_list = ListNode(val=None)
        tail = output_list
        carry = 0
        start = 0
        while l1 != None and l2 != None:
            each_sum = l1.val + l2.val + carry
            if output_list.val == None:
                output_list.val = each_sum%10
                tail = output_list
            else:
                new_node = ListNode(val=each_sum%10)
                tail.next = new_node
                tail = tail.next
            carry = int(each_sum/10)
            l1 = l1.next
            l2 = l2.next
        if l1 != None:
            self.add_pending(l1, carry, output_list, tail)
        elif l2 != None:
            self.add_pending(l2, carry, output_list, tail)
        else:
            if carry != 0:
                new_node = ListNode(val=carry)
                tail.next = new_node
                tail = tail.next
                # output_list.append(carry)
        return output_list
                