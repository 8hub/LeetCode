from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        p_arr = [0 for _ in range(len(nums))]
        n_arr = [0 for _ in range(len(nums))]

        for idx, num in enumerate(nums):
            if num > 0:
                if p_arr[idx-1] > 0:
                    p_arr[idx] = p_arr[idx-1]*num
                    # can update max
                else:
                    p_arr[idx] = num

                if n_arr[idx-1] < 0:
                    n_arr[idx] = n_arr[idx-1]*num
                else:
                    n_arr[idx] = 0
            if num < 0:
                if n_arr[idx-1] < 0:
                    p_arr[idx] = n_arr[idx-1]*num
                    # can update max
                else:
                    p_arr[idx] = 0

                if p_arr[idx-1] > 0:
                    n_arr[idx] = p_arr[idx-1]*num
                else:
                    n_arr[idx] = num
        return max(p_arr)



sol = Solution()
print(sol.maxProduct([2,3,-2,4]))           # 6
print(sol.maxProduct([-2,0,-1]))            # 0
print(sol.maxProduct([-2,3,-2,0,5,2,-1]))   # 12
print(sol.maxProduct([-2,-1]))              # 2
print(sol.maxProduct([-2]))                 # -2