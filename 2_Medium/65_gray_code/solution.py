from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        # nums = [bin(num ^ (num >> 1)) for num in range(2**n)]
        
        # operate on two arrays num [0,1,2,3, ... , 2**n]
        # 1. shift every bit one to right by (num >> 1)
        # 2. (shifted num) XOR (not shifter num) => GRAY CODE
        nums = [(num >> 1) ^ num  for num in range(2**n)]
        return nums
        


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    assert sol.grayCode(2) == [0, 1, 3, 2], "Example 1 failed"

    # Example 2
    assert sol.grayCode(1) == [0, 1], "Example 2 failed"

    # n = 0: only one code
    assert sol.grayCode(0) == [0], "n=0 failed"

    # n = 3: standard sequence
    assert sol.grayCode(3) == [0, 1, 3, 2, 6, 7, 5, 4], "n=3 failed"

    print("All tests passed!")