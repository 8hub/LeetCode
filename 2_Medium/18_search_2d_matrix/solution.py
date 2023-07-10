from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target>matrix[-1][-1] or target < matrix[0][0]:
            return False
        row_nr = self.binarySearchRow([matrix[i][-1] for i in range(len(matrix))], target)
        return self.contain_element(matrix[row_nr],target)
    
    def binarySearchRow(self, array:List[int], target:int):
        top = 0
        bot = len(array)-1
        while(top<bot):
            row = (bot+top)//2
            if(array[row] >= target):
                bot = row
            elif(array[row] < target):
                top = row+1
        return (bot+top)//2

    def contain_element(self,matrix: List[List[int]], target: int) -> bool:
        try:
            matrix.index(target)
            return True
        except ValueError:
            return False

s = Solution()
print(s.searchMatrix([[-1,2,4,5,6],[7,7,7,7,8],[10,16,20,100,101]], -5))
print(s.searchMatrix([[-1,2,4,5,6],[7,7,7,7,8],[10,16,20,100,101]], 9))
print(s.searchMatrix([[-1,2,4,5,6],[7,7,7,7,8],[10,16,20,100,101]], -12))
print(s.searchMatrix([[-1,2,4,5,6],[7,7,7,7,8],[10,16,20,100,101]], 7))
print(s.searchMatrix([[-1,2,4,5,6],[7,7,7,7,8],[10,16,20,100,101]], 2))
print(s.searchMatrix([[-1,2,4,5,6],[7,7,7,7,8],[10,16,20,100,101]], -1))
print(s.searchMatrix([[-1,2,4,5,6],[7,7,7,7,8],[10,16,20,100,101]], 6))
print(s.searchMatrix([[-1,2,4,5,6],[7,7,7,7,8],[10,16,20,100,101]], 101))