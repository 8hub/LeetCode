# from collections import Counter
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # solution 3 O(N) - its ok
        flags = {}
        for idx, elem in enumerate(nums):
            flags[elem] = flags.get(elem,0) + 1
            if flags[elem] > 1:
                return elem
        # # solution 2 -> not enough memory in Counter
        # ctr = Counter(nums)
        # return ctr.keys()
        
        # #solution 1 -> to slow O(N^2)
        # for idx, each in enumerate(nums):
        #     if each in nums[idx+1:]:
        #         return each
        
s = Solution()
print(s.findDuplicate([1,3,4,2,2]))
print(s.findDuplicate([3,1,3,4,2]))