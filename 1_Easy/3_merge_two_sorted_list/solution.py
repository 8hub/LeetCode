from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # # Iterative solution

        # if(list1 == None and list2 == None):
        #     return list1
        # elif (list1 == None):
        #     return list2
        # elif (list2 == None):
        #     return list1
        # merged_list = ListNode()
        # ptr = merged_list        #this is a pointer
        # while list1 and list2 :
        #     if list1.val < list2.val:
        #         ptr.next = list1
        #         list1 = list1.next
        #     else:
        #         ptr.next = list2
        #         list2 = list2.next
        #     ptr = ptr.next
        # if list2:
        #     ptr.next = list2
        # elif list1:
        #     ptr.next = list1
        # return merged_list.next

        # # Recursive solution
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

s = Solution()
print(s.mergeTwoLists(ListNode(1,ListNode(2,ListNode(4))),ListNode(1,ListNode(3,ListNode(4)))))
print(s.mergeTwoLists(ListNode(),ListNode()))
print(s.mergeTwoLists(ListNode(),ListNode(1)))