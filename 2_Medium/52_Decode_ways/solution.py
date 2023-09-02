class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1
        dp[1] = 1
        if s[0] == "0":
            return []
        for idx in range(1,len(s)):
            if s[idx] == '0':
                if s[idx-1] == '1' or s[idx-1] == '2':
                    dp[idx+1] = dp[idx-1]
                else:
                    return []
            else:
                    # eg. ..23.. , ..19.. - there are two possibilities
                if s[idx-1] == '1' or (s[idx-1] == '2' and s[idx] <= '6'):
                    dp[idx+1] = dp[idx-1] + dp[idx]
                    # eg. ..98.. , ..29.. - there are one possibility
                else:
                    dp[idx+1] = dp[idx]
        return dp[-1]
                
        

s = Solution()
print(s.numDecodings("12"))     # == 2
print(s.numDecodings("226"))    # == 3
print(s.numDecodings("0"))      # == 0
print(s.numDecodings("06"))     # == 0
print(s.numDecodings("10"))     # == 1
print(s.numDecodings("101"))    # == 1
print(s.numDecodings("1010"))   # == 1
print(s.numDecodings("1000"))   # == 0
print(s.numDecodings("777"))    # == 1
print(s.numDecodings("111111111111111111111111111111111111111111111"))    # == 1836311903