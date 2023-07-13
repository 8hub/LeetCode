from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        checked = [False for i in range(len(nums))]
        subarr = []
        def dfs():
            if len(subarr) == len(nums):
                ans.append(subarr.copy())
                return
            for i in range(len(nums)):
                if checked[i] == True:
                    continue
                checked[i] = True
                subarr.append(nums[i])
                dfs()
                checked[i] = False
                subarr.pop()
        dfs()
        return ans
    
s = Solution()
print(s.permute([1,2,3]))