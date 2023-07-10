from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        l, r = 0, 0
        while(r < len(height)-1):
            temp_r_highest = r
            while height[l] >= height[temp_r_highest]:
                if(temp_r_highest < length) and (height[l] >= height[temp_r_highest]):
                    temp_r_highest += 1
                if(height[temp_r_highest] > height[r]):
                    r = temp_r_highest