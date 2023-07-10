from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        histogram_len = len(heights)
        stack_height = [heights[0]]
        stack_width = [[0,1]] # pair of starting position and width
        # highest_area = heights[0]
        for index, bar in enumerate(heights):
            try:
                if(heights[index+1] >= stack_height[-1]):
                    stack_width[-1][1] += 1
                    if(heights[index+1] > stack_height[-1]*stack_width[-1][1]):
                        stack_width.append([index, 1])
                        stack_height.append(bar)
                else:
                    pass
            except(IndexError):
                return stack_height[-1]*stack_width[-1][1]
            