from typing import List
import heapq
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

class KthLargest:
    """
    Used min-heap, so the smallest element is always at index 0
    """
    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k 

        heapq.heapify(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

kthLargest = KthLargest(3, [1, 4, 2, 2, 3, 6, 9])
print(kthLargest.add(3))  # Output: 4
print(kthLargest.add(5))  # Output: 5
print(kthLargest.add(10)) # Output: 6
print(kthLargest.add(9))  # Output: 9
print(kthLargest.add(4))  # Output: 9