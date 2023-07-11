from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        sub_array = []
        def dfs(idx):
            if idx >= len(candidates) or sum(sub_array) > target:
                return
            if sum(sub_array) == target:
                ans.append(sub_array.copy())
                return
            
            sub_array.append(candidates[idx])
            dfs(idx)
            sub_array.pop()
            dfs(1+idx)
        dfs(0)
        return ans

s = Solution()
print(s.combinationSum([1,2,3,4],3))
print(s.combinationSum([2,3,6,7],7))
print(s.combinationSum([2,3,5],8))
print(s.combinationSum([2],1))