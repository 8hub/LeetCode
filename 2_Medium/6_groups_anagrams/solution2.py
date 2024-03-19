from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol_dict = {}
        for each in strs:
            key = ''.join(sorted(each))
            sol_dict[key] = sol_dict.get(key, []) + [each]
        return sol_dict.values()





sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(sol.groupAnagrams([""]))
print(sol.groupAnagrams(["a"]))
print(sol.groupAnagrams([]))