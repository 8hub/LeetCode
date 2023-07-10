
class Solution:
    def __init__(self):
        self.board = None
        
    def is_valid(self, x, y, num):
        #check if in row or column is already a num
        for i in range(9):
            if self.board[y][i] == num or self.board[i][x] == num:
                return False

        #check if in square 3x3 is already a num
        x0 = x // 3 * 3
        y0 = y // 3 * 3
        for i in range(3):
            for j in range(3):
                if self.board[y0+i][x0+j] == num:
                    return False
        return True

    def solve_helper(self):
        for x in range(9):
            for y in range(9):
                if self.board[y][x] == ".":
                    for num in "123456789":
                        if self.is_valid(x, y, num):
                            self.board[y][x] = num
                            if self.solve_helper():
                                return True
                            self.board[y][x] = "."
                    return False
        return True

    def printSolved(self):
        for y in range(9):
            for x in range(9):
                print(self.board[y][x], end = " ")
                if x == 2 or x == 5:
                    print("|", end = " ")
            print()
            if y == 2 or y == 5:
                print("-"*21)
            
    def solveSudoku(self, board: list[list[str]]) -> None:
        self.board = board
        self.solve_helper()

board_1 = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

solve = Solution()
print(solve.solveSudoku(board_1))