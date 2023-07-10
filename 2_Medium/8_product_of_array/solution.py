from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all_product = 1
        zeros_counter = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if(zeros_counter == 0):
                    first_zero_index = i
                zeros_counter += 1
            else:
                all_product *= nums[i]
        if zeros_counter >= 2:
            answer = [0 for i in range(len(nums))]
        elif zeros_counter == 1:
            answer = [0 for i in range(len(nums))]
            answer[first_zero_index] = all_product
        else:
            answer = list(map(lambda x: all_product//x, nums))
        return answer
        
s = Solution()
assert s.productExceptSelf([1,2,3,4]) == [24,12,8,6]
assert s.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]