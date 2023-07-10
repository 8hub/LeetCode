class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        index_l = 0
        while (index_l < len(nums)):
            try:
                to_find = target-nums[index_l]
                index_r = nums.index(to_find)
                if(to_find == nums[index_r] and index_r != index_l):
                    return [index_l, index_r]
                index_l += 1
            except:
                index_l += 1
        return [index_l, index_r]