import pandas as pd
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        temp_matrix = matrix.copy()
        for i in range(len(matrix)):
            temp_matrix[i] = matrix[i].copy()
        for y in range(len(matrix)):
            for x in range(len(matrix)):
                matrix[x][-1-y] = temp_matrix[y][x]
        return matrix

### using pandas library nad 'transpose()' method
# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         print(matrix)
#         temp_matrix_df = pd.DataFrame(matrix).transpose()
#         temp_matrix_list = temp_matrix_df.values.tolist()
#         print(temp_matrix_list)
#         for i in range(len(temp_matrix_list)):
#             matrix[i] = temp_matrix_list[i][::-1]