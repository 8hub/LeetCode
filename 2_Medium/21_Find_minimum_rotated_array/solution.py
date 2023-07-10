from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        lp = 0
        rp = len(nums)-1
        while(lp <= rp):
            mid = (lp+rp)//2
            if(nums[mid] >= nums[lp]) and (nums[rp] < nums[mid]):
                lp = mid+1
            elif(nums[mid] < nums[rp]) and (nums[mid] < nums[lp]):
                rp = mid
            # elif(nums[mid] < nums[lp]) and (nums[mid] > nums[rp]):
            #     rp = mid
            # rising sequence
            elif(nums[mid] >= nums[lp]) and (nums[mid] <= nums[rp]):
                return nums[lp]
            elif(nums[lp] == nums[rp]):
                return nums[mid]
        return nums[mid]
    
s = Solution()
print(s.findMin([3,4,5,1,2]))       #1
print(s.findMin([4,5,6,7,0,1,2]))   #0
print(s.findMin([11,13,15,17]))     #11
print(s.findMin([11,1]))            #1
print(s.findMin([1]))            #1
