from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_all = len(nums)
        left_part = [1 for x in range(len_all)]
        right_part = left_part.copy()
        solution = left_part.copy()
        for idx in range(len_all-1):
            left_part[idx+1] = left_part[idx]*nums[idx]
            right_part[len_all-idx-2] = right_part[len_all-1-idx]*nums[len_all-1-idx]
        for idx in range(len_all):
            solution[idx] = left_part[idx]*right_part[idx]
        return solution
    
sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))
print(sol.productExceptSelf([-1,1,0,-3,3]))