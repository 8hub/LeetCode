from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = {}
        for each in nums:
            nums_count[each] = nums_count.get(each,0)+1
        nums_count_items = sorted(nums_count.items(),key=lambda x:x[1], reverse=True)
        return [it[0] for it in nums_count_items][:k]
        
s = Solution()
print(s.topKFrequent([1,1,1,1,2,2,3,4,4,4], 4))