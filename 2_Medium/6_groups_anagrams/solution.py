from typing import List
from collections import defaultdict
# from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initializes a list as a value when there is no exisiting key
        hash_anagrams = defaultdict(list)
        for each in strs:
            current_letters_list = list(each)
            current_letters_list.sort()
            current_letters_tuple = tuple(current_letters_list)
            hash_anagrams[current_letters_tuple].append(each)
        return hash_anagrams.values()
        
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if(len(s) != len(t)): return False
    #     counter_s, counter_t = {}, {}
    #     for i in range(len(s)):
    #         counter_s[s[i]] = counter_s.get(s[i],0) + 1
    #         counter_t[t[i]] = counter_t.get(t[i],0) + 1
    #     return counter_s == counter_t

s = Solution()
print(s.groupAnagrams(["eatt","ttea","tan","ate","nat","bat"]))