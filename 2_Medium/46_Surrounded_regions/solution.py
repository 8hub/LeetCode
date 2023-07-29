from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        max_idx_x = len(board[0])-1
        max_idx_y = len(board)-1
        
        # Run markEscapes just for board squares
        def markEscapes(pos_y, pos_x):
            # Out of boundries
            if (pos_x >= len(board[0])) or (pos_y >= len(board)) or (pos_x < 0) or (pos_y < 0) or board[pos_y][pos_x] == 'E' or board[pos_y][pos_x] == 'X':
                return
            
            if board[pos_y][pos_x] == 'O':
                board[pos_y][pos_x] = 'E'

            markEscapes(pos_y, pos_x-1)
            markEscapes(pos_y, pos_x+1)
            markEscapes(pos_y-1, pos_x)
            markEscapes(pos_y+1, pos_x)


        for x in range(len(board[0])):
            if board[0][x] == 'O':
                markEscapes(0,x)
            if board[max_idx_y][x] == 'O':
                markEscapes(max_idx_y, x)

        for y in range(len(board)):
            if board[y][0] == 'O':
                markEscapes(y,0)
            if board[y][max_idx_x] == 'O':
                markEscapes(y, max_idx_x)

        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == 'O':
                    board[y][x] = 'X'
                elif board[y][x] == 'E':
                    board[y][x] = 'O'

        return board
        
    

s = Solution()
print(s.solve([["X","O","X"],
               ["O","X","O"],
               ["X","O","X"]]))

print(s.solve([["O","O","O","O","X","X"],
               ["O","O","O","O","O","O"],
               ["O","X","O","X","O","O"],
               ["O","X","O","O","X","O"],
               ["O","X","O","X","O","O"],
               ["O","X","O","O","O","O"]]))

print(s.solve([["X","X","X","X"],
               ["X","O","O","X"],
               ["X","X","O","X"],
               ["X","O","X","X"]]))

print(s.solve([["O","O","O","O"],
               ["O","O","O","O"],
               ["O","O","O","O"],
               ["O","O","O","O"]]))

print(s.solve([["X"]]))