from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []      # pair [temperatures[0],0]
        ans = [0] * len(temperatures)
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_index = stack.pop()[1]
                ans[stack_index] = index-stack_index
            stack.append([temp,index])
        # while stack:
        #     ans[stack.pop()[1]] = 0
        return ans
    
s = Solution()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))