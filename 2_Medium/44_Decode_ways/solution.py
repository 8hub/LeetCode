class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        dp = [0] * (len(s) + 1)
        dp[0] = dp[1] = 1
        
        for i in range(2, len(s) + 1):
            if 1 <= int(s[i-1:i]) <= 9:     # single digit
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26:   # double digit
                dp[i] += dp[i-2]
        return dp[len(s)]


test = Solution()
print(test.numDecodings("12"))
print(test.numDecodings("226"))
print(test.numDecodings("06"))
print(test.numDecodings("111111"))
