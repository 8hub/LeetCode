import unittest
from typing import List

class Solution:
    DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)] # right, down, left, up

    def generateMatrix(self, n: int) -> List[List[int]]:
        TOTAL_CELLS = n * n
        matrix = [[0] * n for _ in range(n)]
        filled_nr = 0
        x_coord = 0
        y_coord = 0
        current_direction = 0       # 0-right, 1-down, 2-left, 3-up
        while filled_nr < TOTAL_CELLS:
            filled_nr += 1
            matrix[y_coord][x_coord] = filled_nr
            ### next direction
            match current_direction:
            # check end of right side
                case 0:
                    if x_coord + 1 >= n or matrix[y_coord][x_coord+1] != 0:
                        current_direction += 1
            # check end of bottom side
                case 1:
                    if y_coord + 1 >= n or matrix[y_coord+1][x_coord] != 0:
                        current_direction += 1
            # check end of left side
                case 2:
                    if x_coord - 1 < 0 or matrix[y_coord][x_coord-1] != 0:
                        current_direction += 1
            # check end of upper side
                case 3:
                    if y_coord - 1 < 0 or matrix[y_coord-1][x_coord] != 0:
                        current_direction = 0

            x_coord += self.DIRECTIONS[current_direction][0]
            y_coord += self.DIRECTIONS[current_direction][1]

        return matrix


if __name__ == '__main__':

    class TestSpiralMatrixII(unittest.TestCase):
        def test_example_1(self):
            sol = Solution()
            self.assertEqual(
                sol.generateMatrix(3),
                [[1, 2, 3],
                 [8, 9, 4],
                 [7, 6, 5]]
            )

        def test_example_2(self):
            sol = Solution()
            self.assertEqual(
                sol.generateMatrix(1),
                [[1]]
            )

        def test_n_2(self):
            sol = Solution()
            self.assertEqual(
                sol.generateMatrix(2),
                [[1, 2],
                 [4, 3]]
            )

        def test_n_4(self):
            sol = Solution()
            self.assertEqual(
                sol.generateMatrix(4),
                [[1,  2,  3,  4],
                 [12, 13, 14, 5],
                 [11, 16, 15, 6],
                 [10, 9,  8,  7]]
            )

        def test_n_5(self):
            sol = Solution()
            self.assertEqual(
                sol.generateMatrix(5),
                [[1,  2,  3,  4,  5],
                 [16, 17, 18, 19, 6],
                 [15, 24, 25, 20, 7],
                 [14, 23, 22, 21, 8],
                 [13, 12, 11, 10, 9]]
            )

    unittest.main(verbosity=2, exit=False)