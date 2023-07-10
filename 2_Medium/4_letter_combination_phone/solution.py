from typing import List
class Solution:
    dig_dict = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        results = ['']
        for digit in digits:
            letters = self.dig_dict[digit]
            results = [res + letter for res in results for letter in letters]
        return results

# class Solution:
#     dig_2 = ['a', 'b', 'c']
#     dig_3 = ['d', 'e', 'f']
#     dig_4 = ['g', 'h', 'i']
#     dig_5 = ['j', 'k', 'l']
#     dig_6 = ['m', 'n', 'o']
#     dig_7 = ['p', 'q', 'r', 's']
#     dig_8 = ['t', 'u', 'v']
#     dig_9 = ['w', 'x', 'y', 'z']
    
#     def letterCombinations(self, digits:str)->List [str]:
#         if digits == '': return []
#         if len(digits) == 1: return self.getLetters(digits[0])
#         final_posibilities = self.getLetters(digits[0])
#         temp1_posibilities = []
#             #256 -> len = 3
#         for iter in range(len(digits)):
#             if iter > 0:
#                 temp1_posibilities = self.combineTwoList(final_posibilities, self.getLetters(digits[iter]))
#                 final_posibilities = temp1_posibilities
#         return final_posibilities
            
#     def getLetters(self, digit:str) -> List[str]:
#         if digit == '2':
#             return self.dig_2
#         elif digit == '3':
#             return self.dig_3
#         elif digit == '4':
#             return self.dig_4
#         elif digit == '5':
#             return self.dig_5
#         elif digit == '6':
#             return self.dig_6
#         elif digit == '7':
#             return self.dig_7
#         elif digit == '8':
#             return self.dig_8
#         else :
#             return self.dig_9
    
#     def combineTwoList(self, list1:List[str], list2:List[str]) -> List[str]:
#         combined = []
#         for iter1 in list1:
#             for iter2 in list2:
#                 combined.append(iter1+iter2)
#         return combined