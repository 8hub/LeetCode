from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #go to end of the each list
        ptr_l1, ptr_l2 = l1, l2
        carry = 0 #indicate if next node should be increased eg. 9+9 = 18 -> carry=1 and val=8
        sum_node = ListNode() #dummy node
        ptr_sum_node = sum_node
        while ptr_l1 and ptr_l2:
            temp_sum = carry + ptr_l1.val + ptr_l2.val
            ptr_sum_node.next = ListNode(temp_sum % 10)
            carry = temp_sum // 10
            ptr_sum_node = ptr_sum_node.next
            ptr_l1 = ptr_l1.next
            ptr_l2 = ptr_l2.next
        #from end create new nodes as a sum of val1 and val2
        while ptr_l1:
            temp_sum = carry + ptr_l1.val
            ptr_sum_node.next = ListNode(temp_sum % 10)
            carry = temp_sum // 10
            ptr_sum_node = ptr_sum_node.next
            ptr_l1 = ptr_l1.next
        while ptr_l2:
            temp_sum = carry + ptr_l2.val
            ptr_sum_node.next = ListNode(temp_sum % 10)
            carry = temp_sum // 10
            ptr_sum_node = ptr_sum_node.next
            ptr_l2 = ptr_l2.next
        if carry > 0:
            ptr_sum_node.next = ListNode(carry)
        return sum_node.next

s = Solution()
l_node1 = ListNode(2,ListNode(4,ListNode(3)))
l_node2 = ListNode(5,ListNode(6,ListNode(4)))
l_node3 = ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9)))))))
l_node4 = ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9)))))
s.addTwoNumbers(l_node1, l_node2)
s.addTwoNumbers(l_node3, l_node4)