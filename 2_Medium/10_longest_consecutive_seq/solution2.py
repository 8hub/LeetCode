from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        if len(numSet) <= 1:
            return len(numSet)
        longest = {}
        for each in numSet:
            if (each-1) not in numSet and each not in longest:
                longest[each] = longest.get(each, 0) + 1
                current = each
                while (current+1) in numSet:
                    longest[each] = longest.get(each, 0) + 1
                    current += 1
        return max(longest.values())

sol = Solution()
print(sol.longestConsecutive([100,4,200,1,3,2]))
print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(sol.longestConsecutive([]))
print(sol.longestConsecutive([1]))
print(sol.longestConsecutive([1,3,2,4,5]))