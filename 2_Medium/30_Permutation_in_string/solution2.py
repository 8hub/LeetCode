from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        base_str_multiset = Counter(s1)
        left_idx, right_idx = 0, len(s1)-1
        length = len(s2)
        check_str_multiset = Counter(s2[:len(s1)-1])
        while right_idx < length:
            check_str_multiset.update(s2[right_idx])
            if base_str_multiset != check_str_multiset:
                check_str_multiset.subtract(s2[left_idx])
                left_idx += 1
                right_idx += 1
            else:
                return True
        return False
    
sol = Solution()
print(sol.checkInclusion("ab", "eidbaooo"))
print(sol.checkInclusion("adc", "dcda"))
print(sol.checkInclusion("ab", "erbae"))
print(sol.checkInclusion("ab", "eidboaoo"))
print(sol.checkInclusion("abcdxabcde", "abcdeabcdx"))