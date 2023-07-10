from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        ptr = head
        #check length of singly-linked list
        while(ptr):
            length +=1
            ptr = ptr.next
        elem_before_del = length - n
        if(elem_before_del == 0):
            return head.next
        ptr = head
        curr_elem = 1
        while(curr_elem < elem_before_del):
            ptr = ptr.next
            curr_elem += 1
        if length == 1:
            ptr = None
        elif length == 2:
            if n == 1:
                ptr.next = None
            else:
                return ptr.next
        else:
            ptr.next = ptr.next.next
        return head
        
s = Solution()
print(s.removeNthFromEnd(ListNode(1),1))
print(s.removeNthFromEnd(ListNode(1,ListNode(2)),1))
print(s.removeNthFromEnd(ListNode(1,ListNode(2)),2))
print(s.removeNthFromEnd(ListNode(1,ListNode(2,ListNode(3))),1))
print(s.removeNthFromEnd(ListNode(1,ListNode(2,ListNode(3))),2))
print(s.removeNthFromEnd(ListNode(1,ListNode(2,ListNode(3))),3))
print(s.removeNthFromEnd(ListNode(1,ListNode(2,ListNode(3,ListNode(4)))),2))
print(s.removeNthFromEnd(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5))))),5))