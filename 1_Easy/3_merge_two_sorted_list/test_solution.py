from solution import Solution
from solution import ListNode

def test_merge1():
    s = Solution()
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    s.mergeTwoLists(list1, list2)