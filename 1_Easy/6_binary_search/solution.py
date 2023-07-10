from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ptr_l = 0
        ptr_r = len(nums)-1
        while(ptr_l <= ptr_r):
            mid = (ptr_l + ptr_r)//2
            if nums[mid] < target:
                ptr_l = mid+1
            elif nums[mid] > target:
                ptr_r = mid-1
            else:
                return mid
        return -1
    
s = Solution()
print(s.search([1, 2, 3, 4, 5, 6], 3))
print(s.search([1, 2, 3, 4, 5, 6], 1))
print(s.search([1, 2, 3, 4, 5, 6], 6))
print(s.search([1, 2, 3, 4, 5, 6, 7], 1))
print(s.search([1, 2, 3, 4, 5, 6, 7], 3))
print(s.search([1, 2, 3, 4, 5, 6, 7], 7))