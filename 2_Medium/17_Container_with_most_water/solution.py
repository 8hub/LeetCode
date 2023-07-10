from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        l = 0               #left pointer
        r = length-1             #right pointer
        max_area = 0
        while l<r:
            max_area = max(max_area,min(height[l],height[r])*(r-l))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max_area
s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
print(s.maxArea([1,1]))
print(s.maxArea([1,0]))
print(s.maxArea([10,10,1]))
print(s.maxArea([10,15,1]))
print(s.maxArea([1,2,3,4,5,6,7,1,2,0]))
print(s.maxArea([1,8,6,2,5,4,8,25,7]))

