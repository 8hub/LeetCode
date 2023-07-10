from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, nextt = None):
        self.val = x
        self.next = nextt

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # # 0 apprach - with N(1) memory
        slow_ptr, fast_ptr = head, head
        while (fast_ptr.next.next.next):
            fast_ptr = fast_ptr.next.next.next.next
            slow_ptr = slow_ptr.next.next.next
            if fast_ptr == slow_ptr:
                return True
        return False
        
        # # 1st approach
        # ptr = head
        # counter = 0
        # while (counter <= 10000):
        #     ptr = ptr.next
        #     counter +=1
        # if counter == 10001:
        #     return True
        # return False
    
        # # 2nd approach
        # ptr = head
        # all_nodes = []
        # while(ptr != None):
        #     if(ptr in all_nodes):
        #         return True
        #     all_nodes.append(ptr)
        #     ptr = ptr.next
        # return False

s = Solution()
s.hasCycle(ListNode(1,ListNode(2,ListNode(4))))
fst = ListNode(1)
scd = ListNode(2,fst)
fst.next = scd
s.hasCycle(fst)