from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums_part: List[int]):
            rob1, rob2 = 0,0
            for n in nums_part:
                newRob = max(rob1+n, rob2)
                rob1 = rob2
                rob2 = newRob
            return rob2
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))

s = Solution()
print(s.rob([2,3,2]))               # 3
print(s.rob([1,2,3,1]))             # 4
print(s.rob([1,2,3]))               # 3
print(s.rob([5,4,2,3,5,8,2]))       # 16
print(s.rob([200,3,140,20,10]))     # 340
print(s.rob([1,3,1,3,100]))         # 103