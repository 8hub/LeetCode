from typing import List
from typing import Counter
class Solution:
    def __init__(self):
        board = [[] for i in range(9)]
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.board = board
        for i in range(9):
            if self.valid_row(i) == False:
                return False
            if self.valid_col(i) == False:
                return False
            if self.valid_3x3_box(i) == False:
                return False
        return True
            
    def valid_3x3_box(self, box_index) -> bool:
        row_begin = (box_index//3)*3
        col_begin = (box_index%3)*3
        counter = {}
        for x in range(3):
            for y in range(3):
                i = self.board[row_begin+x][col_begin+y]
                if i != '.':
                    counter[i] = 1 + counter.get(i, 0)
                    if counter[i] > 1:
                        return False
        return True
                
    def valid_col(self, col_index) -> bool:
        counter = {}
        for each in range(9):
            i = self.board[each][col_index]
            if i != '.':
                counter[i] = 1 + counter.get(i, 0)
                if counter[i] > 1:
                    return False
        return True
     
    def valid_row(self, row_index) -> bool:
        counter = {}
        for i in self.board[row_index]:
            if i != '.':
                counter[i] = 1 + counter.get(i, 0)
                if counter[i] > 1:
                    return False
        return True
    def make_list(self) -> list:
        
        
s =  Solution()
print(s.isValidSudoku([
["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
print(s.isValidSudoku([
["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
print(s.isValidSudoku([
[".",".","4",".",".",".","6","3","."],
[".",".",".",".",".",".",".",".","."],
["5",".",".",".",".",".",".","9","."],
[".",".",".","5","6",".",".",".","."],
["4",".","3",".",".",".",".",".","1"],
[".",".",".","7",".",".",".",".","."],
[".",".",".","5",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."]]))