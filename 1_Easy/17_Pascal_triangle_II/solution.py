from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        ans = [1]
        for row in range(rowIndex):
            temp = [0] + ans + [0]
            for idx in range(len(temp)-1):
                temp[idx] = temp [idx] + temp[idx+1]
            ans = temp[:-1]
        return ans
sol = Solution()

print(sol.getRow(0))
print(sol.getRow(1))
print(sol.getRow(2))
print(sol.getRow(3))
print(sol.getRow(4))
print(sol.getRow(5))