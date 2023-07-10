
from typing import List
class Solution:
    def longestConsecutive(nums: List[int]) -> int:
        contain_nr = sorted(set(nums))
        if len(contain_nr) == 1:
            return 1
        if len(contain_nr) == 0:
            return 0
        longest_seq = 0
        curr_seq = 1
        for each in range(len(contain_nr)-1):
            if contain_nr[each] == contain_nr[each+1]-1:
                curr_seq += 1
            else:
                curr_seq = 1
            longest_seq = max(longest_seq, curr_seq)
        return longest_seq
    
s = Solution
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(s.longestConsecutive([100,4,200,1,3,2]))
print(s.longestConsecutive([1,1,1]))
print(s.longestConsecutive([1]))
print(s.longestConsecutive([]))