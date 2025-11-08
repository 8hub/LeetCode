# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == None or lists == ListNode(None):
            return None
        
        dummy = ListNode()
        tail = dummy
        continue_checking = True

        while continue_checking:
            continue_checking = False
            first_check = True
            smallest_node_nr = 0
            for list_nr, curr_list in enumerate(lists):
                if curr_list != None:
                    continue_checking = True
                    if first_check:
                        smallest_node_nr = list_nr
                        first_check = False
                    elif curr_list.val < lists[smallest_node_nr].val:
                        smallest_node_nr = list_nr

            if continue_checking:
                tail.next = lists[smallest_node_nr]
                lists[smallest_node_nr] = lists[smallest_node_nr].next
                tail = tail.next
                
        return dummy.next


if __name__ == '__main__':
    def build_list(nums: List[int]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        for n in nums:
            cur.next = ListNode(n)
            cur = cur.next
        return dummy.next

    def list_to_arr(head: Optional[ListNode]) -> List[int]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res

    # Example 1
    lists1 = [
        build_list([1, 4, 5]),
        build_list([1, 3, 4]),
        build_list([2, 6])
    ]
    result1 = Solution().mergeKLists(lists1)
    assert list_to_arr(result1) == [1, 1, 2, 3, 4, 4, 5, 6], "Example 1 failed"

    # Example 2
    lists2: List[Optional[ListNode]] = []
    result2 = Solution().mergeKLists(lists2)
    assert list_to_arr(result2) == [], "Example 2 failed"

    # Example 3
    lists3 = [None]  # represents [[]]
    result3 = Solution().mergeKLists(lists3)
    assert list_to_arr(result3) == [], "Example 3 failed"

    # Single list
    lists_single = [build_list([1, 3, 5])]
    assert list_to_arr(Solution().mergeKLists(lists_single)) == [1, 3, 5]


    # Duplicates across lists
    lists_dup = [build_list([1, 1]), build_list([1])]
    assert list_to_arr(Solution().mergeKLists(lists_dup)) == [1, 1, 1]

    print("All tests passed!")