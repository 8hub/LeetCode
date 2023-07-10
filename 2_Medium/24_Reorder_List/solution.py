from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ptr_slow = head
        ptr_fast = head.next
        # 1 - create a 2nd ListNode from middle
        # if ptr_fast == None there are odd nr of elements
        # if ptr_fast.next == None there are even nr of elements
        while (ptr_fast) and (ptr_fast.next):
            ptr_slow = ptr_slow.next
            ptr_fast = ptr_fast.next.next
        ptr_left = head
        ptr_slow2 = ptr_slow.next   # here the ptr_slow.next is Node assigned to ptr_slow2
        ptr_slow.next = None        # here the ptr_slow.next is pointer pointing to next Node
                                    # so we can brake the link here not affecting the ptr_slow2
        # 2 - reverse 2nd List
        #ptr_right is reversed ListNode from middle of the head
        ptr_right = ListNode(None)
        while ptr_slow2:
            temp_node = ptr_slow2.next
            ptr_right = ListNode(ptr_slow2.val, ptr_right)
            ptr_slow2 = temp_node
        # 3 - merge two halves
        # merging is ok, but after creating final Linked list
        # its end contain rest of right half of primary head List - to correct
        while (ptr_right.val):
            temp1, temp2 = ptr_left.next, ptr_right.next
            ptr_left.next = ptr_right
            ptr_right.next = temp1
            ptr_left = temp1
            ptr_right = temp2
    
s = Solution()
print(s.reorderList(ListNode(1,ListNode(2,ListNode(3,ListNode(4))))))
print(s.reorderList(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))))