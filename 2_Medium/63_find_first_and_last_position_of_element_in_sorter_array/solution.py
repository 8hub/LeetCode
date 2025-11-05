from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: return [-1,-1]
        res = [-1,-1]
        l_ptr, r_ptr = 0, len(nums)-1
        
        # find left occurance
        while l_ptr < r_ptr:
            mid_ptr = (l_ptr + r_ptr) // 2
            if nums[mid_ptr] >= target:
                r_ptr = mid_ptr
            else:
                l_ptr = mid_ptr + 1
                
        if nums[l_ptr] == target:
            res[0] = l_ptr

        l_ptr, r_ptr = 0, len(nums) - 1
        
        # find right occurance
        while l_ptr < r_ptr:
            mid_ptr = (l_ptr + r_ptr + 1) // 2
            if nums[mid_ptr] <= target:
                l_ptr = mid_ptr
            else:
                r_ptr = mid_ptr - 1
                
        if nums[r_ptr] == target:
            res[1] = r_ptr

        return res




if __name__ == "__main__":
    sol = Solution()

    # Example 1: Target exists with duplicates
    assert sol.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4], 'Test 1 Failed'

    # Example 2: Target does not exist
    assert sol.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]

    # Example 3: Empty array
    assert sol.searchRange([], 0) == [-1, -1]

    # Single element: target found
    assert sol.searchRange([1], 1) == [0, 0]

    # Single element: target not found
    assert sol.searchRange([1], 2) == [-1, -1]

    # Target at the beginning (all same)
    assert sol.searchRange([1, 1, 1, 1], 1) == [0, 3]

    # Target at the end
    assert sol.searchRange([1, 2, 3, 3, 3, 4], 3) == [2, 4]

    # All elements are target
    assert sol.searchRange([5, 5, 5, 5, 5], 5) == [0, 4]

    # Target appears only once in the middle
    assert sol.searchRange([1, 2, 3, 4, 5], 3) == [2, 2]

    # Target not present in large sorted array
    assert sol.searchRange([1, 2, 3, 4, 5, 6, 7, 8, 9], 10) == [-1, -1]

    print("All tests passed!")