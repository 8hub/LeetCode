from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(list(set(nums)))
        nr_elements = len(nums)
        answer = []
        for check in range(nr_elements):
            l, r = 0, nr_elements-1
            # if (check - 1 >= 0) and (nums[check-1] == nums[check]):
            #     continue
            while (l < r):
                if(l == check or r == check):
                    break
                if(nums[l] + nums[r] + nums[check] > 0):
                    r -= 1
                elif(nums[l] + nums[r] + nums[check] < 0):
                    l += 1
                elif(nums[l] + nums[r] + nums[check] == 0):
                    if [nums[l],nums[check],nums[r]] not in answer:
                        answer.append([nums[l],nums[check],nums[r]])
                    l += 1
        return answer

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
print(s.threeSum([0,1,1]))
print(s.threeSum([0,0,0,0]))
print(s.threeSum([-1,2,3,-5,-1,5,0,0,0,0,0]))
print(s.threeSum([3,0,-2,-1,1,2]))
print(s.threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))