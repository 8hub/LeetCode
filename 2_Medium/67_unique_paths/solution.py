import unittest

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memory = [[0 for _ in range(n)] for _ in range(m)]
        def dp(row: int, column: int) -> int:
            # just one possibility on last column and last row
            if row == m - 1 or column == n - 1:
                return 1
            if memory[row][column] != 0:
                return memory[row][column]

            down = dp(row + 1, column)
            right = dp(row, column + 1)
            memory[row][column] = down + right
            return memory[row][column]

        return dp(0,0)

            

class TestUniquePaths(unittest.TestCase):
    def test_example_1(self):
        sol = Solution()
        self.assertEqual(sol.uniquePaths(3, 2), 3)

    def test_example_2(self):
        sol = Solution()
        self.assertEqual(sol.uniquePaths(3, 7), 28)

    def test_single_row(self):
        sol = Solution()
        self.assertEqual(sol.uniquePaths(1, 5), 1)

    def test_single_column(self):
        sol = Solution()
        self.assertEqual(sol.uniquePaths(5, 1), 1)

    def test_1x1_grid(self):
        sol = Solution()
        self.assertEqual(sol.uniquePaths(1, 1), 1)

if __name__ == '__main__':
    unittest.main(verbosity=2)