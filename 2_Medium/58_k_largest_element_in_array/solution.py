import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # convert k largest to n smallest
        n = len(nums) - k + 1
        heapq.heapify(nums)
        while n > 1:
            heapq.heappop(nums)
            n -= 1
        return nums[0]
    
sol = Solution()
print(sol.findKthLargest([3,2,1,5,6,4],2))
print(sol.findKthLargest([3,2,3,1,2,4,5,5,6],4))