class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        l, r = 0, 0
        max_len = 0
        while (r+1<len(s)):
            while (r+1 < len(s)) and (s[r+1] in s[l:r+1]) and (l <= r):
                if l == r:
                    l += 1
                    r += 1
                else:
                    l += 1
            while (r+1 < len(s)) and (s[r+1] not in s[l:r+1]):
                r += 1
            max_len = max(max_len, r-l+1)
        return max_len
                
s = Solution()
print(s.lengthOfLongestSubstring("abcaabcbb"))
print(s.lengthOfLongestSubstring("bbbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))