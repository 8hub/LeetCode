from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # iterative solution
        # ans = None
        # while(head):
        #     temp = head.next    #remember rest of head (without head[0])
        #     head.next = ans     #append val of head with answer head[0]->ans
        #     ans = head          #update answer = head[0]->ans
        #     head = temp         #head = head.next
        # return ans

        # # iterative solution v2
        # ans = None
        # while(head):
        #     # temp = head.next
        #     ans = ListNode(head.val,ans)
        #     head = head.next
        # return ans
    
        # recursive solution
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead
    
s = Solution()
s.reverseList(ListNode(1,ListNode(2,ListNode(3,ListNode(4)))))
pass