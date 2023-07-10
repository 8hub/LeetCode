from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] == target:
            return 0
        lp = 0
        rp = len(nums)-1
        while (lp <= rp):
            mid = (lp + rp)//2
            if(nums[mid] > target) and (nums[lp] <= target):
                rp = mid
            elif(nums[mid] > target) and (nums[lp] > target) and (nums[mid] >= nums[lp]):
                lp = mid + 1
            elif(nums[mid] > target) and (nums[lp] > target) and (nums[mid] <= nums[lp]):
                rp = mid
            elif(nums[mid] < target) and (nums[lp] < target) and (nums[mid] >= nums[lp]):
                lp = mid + 1
            elif(nums[mid] < target) and (nums[lp] < target) and (nums[mid] <= nums[lp]):
                rp = mid
            elif(nums[mid] < target) and (nums[rp] >= target):
                lp = mid + 1
            elif(nums[mid] < target) and (nums[rp] <= target):
                rp = mid
            elif(nums[lp]> target) and (nums[rp] < target):
                return -1
            elif(nums[mid]==target):
                return mid
        return -1 

s = Solution()
print(s.search([3,4,5,1,2],1))       #3
print(s.search([4,5,6,7,0,1,2],0))   #4
print(s.search([3,4,5,1,2],1))       #3
print(s.search([4,5,6,7,9,0,1,2],9)) #4
print(s.search([4,5,6,7,0,1,2],3))   #-1
print(s.search([6,7,0,1,2,3,4,5],3)) #5
print(s.search([1,3],2))             #-1
print(s.search([5,1,3],3))           #2
print(s.search([5,1,2,3,4],1))       #1
print(s.search([8,9,2,3,4],9))       #1