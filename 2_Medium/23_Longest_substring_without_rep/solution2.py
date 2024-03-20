class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        start_idx, end_idx, length = 0, 1, len(s)
        subset = set(s[start_idx])
        max_len = 1
        while end_idx < length:
            if s[end_idx] not in subset:
                subset.add(s[end_idx])
                end_idx += 1
                max_len = max(max_len, len(subset))
            else:
                subset.remove(s[start_idx])
                start_idx += 1
        return max_len

sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("bbbbb"))
print(sol.lengthOfLongestSubstring("pwwkew"))
print(sol.lengthOfLongestSubstring("pweewera"))