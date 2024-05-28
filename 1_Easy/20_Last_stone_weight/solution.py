from typing import List
import heapq

class Solution:
    def lastStoneWeigth(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            if stones[0] == stones[1]:
                print("==", stones)
                heapq.heappop(stones)
                heapq.heappop(stones)
            else:
                print("!=", stones)
                leftover = heapq.heappop(stones) - heapq.heappop(stones)
                heapq.heappush(stones, leftover)
        if stones:
            return -stones[0]
        return 0
    

sol = Solution()
print(sol.lastStoneWeigth([2,7,4,1,8,1]))