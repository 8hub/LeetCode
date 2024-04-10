from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        curr = []
        for each in range(numRows):
            curr.append(1)
            curr_idx = 1
            while curr_idx <= (len(curr)+1)/2-1:
                curr[curr_idx] = ans[-1][curr_idx] + ans[-1][curr_idx-1]
                curr[-curr_idx-1] = curr[curr_idx]
                curr_idx += 1
            ans.append(curr.copy())
        return ans

sol = Solution()
print(sol.generate(1))
print(sol.generate(2))
print(sol.generate(3))
print(sol.generate(4))
print(sol.generate(10))
print(sol.generate(30))