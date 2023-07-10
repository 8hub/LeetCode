from typing import List
class Solution:
    def containsDuplicate(self, nums:List[int]) ->bool:
        nums.sort()
        for index, elem in enumerate(nums[:-1]):
            if(nums[index] == nums[index+1]):
                return True
        return False