from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        ans = head.next
        ln_1, ln_2 = head, head.next

        while ln_2 != None:
            # Swap two nodes
            ln_temp = ln_2.next
            ln_2.next = ln_1
            # Check if there are next to nodes to swap
            if ln_temp != None and ln_temp.next != None:
                ln_1.next = ln_temp.next
                ln_1 = ln_temp
                ln_2 = ln_temp.next
            else:
                ln_1.next = ln_temp
                break

        return ans

# Helper: Convert list to linked list
def create_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# Helper: Convert linked list to Python list for easy comparison
def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# === TEST SUITE ===

if __name__ == "__main__":
    solution = Solution()

    # Test 1: Even length list
    head = create_list([1, 2, 3, 4])
    expected = [2, 1, 4, 3]
    result = solution.swapPairs(head)
    assert to_list(result) == expected, f"Test 1 failed: Expected {expected}, got {to_list(result)}"

    # Test 2: Odd length list
    head = create_list([1, 2, 3])
    expected = [2, 1, 3]
    result = solution.swapPairs(head)
    assert to_list(result) == expected, f"Test 2 failed: Expected {expected}, got {to_list(result)}"

    # Test 3: Empty list
    head = create_list([])
    expected = []
    result = solution.swapPairs(head)
    assert to_list(result) == expected, f"Test 3 failed: Expected {expected}, got {to_list(result)}"

    # Test 4: Single node
    head = create_list([1])
    expected = [1]
    result = solution.swapPairs(head)
    assert to_list(result) == expected, f"Test 4 failed: Expected {expected}, got {to_list(result)}"

    # Test 5: Two nodes
    head = create_list([5, 10])
    expected = [10, 5]
    result = solution.swapPairs(head)
    assert to_list(result) == expected, f"Test 5 failed: Expected {expected}, got {to_list(result)}"

    # Test 6: Long even list
    head = create_list([1, 2, 3, 4, 5, 6, 7, 8])
    expected = [2, 1, 4, 3, 6, 5, 8, 7]
    result = solution.swapPairs(head)
    assert to_list(result) == expected, f"Test 6 failed: Expected {expected}, got {to_list(result)}"

    print("All tests passed!")