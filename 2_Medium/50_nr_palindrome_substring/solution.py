class Solution:
    def sameChars(self, letter1: str, letter2: str):
        return letter1 == letter2
    
    def countSubstrings(self, s: str) -> int:
        counter = 0
        s_len = len(s)
        for idx in range(s_len):
            i = 0
            while (idx-i >= 0) and (idx+i < s_len) and self.sameChars(s[idx-i],s[idx+i]):
                counter += 1
                i += 1
            i = 0
            while (idx-i >=0) and (idx+1+i < s_len) and self.sameChars(s[idx-i], s[idx+1+i]):
                counter += 1
                i += 1
        return counter
    
s = Solution()
assert s.countSubstrings('abc') == 3
assert s.countSubstrings('aaa') == 6
assert s.countSubstrings('a') == 1