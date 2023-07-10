from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter = 0
        length = len(grid)
        for row in range(length):
            iterator_col = 0
            while(iterator_col < length):
                if([grid[i][iterator_col] for i in range(len(grid))] == grid[row]):
                    counter += 1
                iterator_col += 1
        return counter
    

s = Solution()
print(s.equalPairs([[3,2,1],[1,7,6],[2,7,7]]))
print(s.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))