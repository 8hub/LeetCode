class Solution:
    def numDecodings(self, s: str) -> int:
        checked = {}
        if not s:
            return 0
        def recursive_decode(s: str, index: int) -> int:
            if index == len(s):
                return 1
            if s[index] == '0':
                return 0
            if index in checked:
                return checked[index]
            
            counter = recursive_decode(s, index + 1)
            
            if index+1 < len(s) and (s[index]=='1' or (s[index]=='2' and s[index+1] in '0123456')):
                counter += recursive_decode(s, index+2)

            checked[index] = counter

            return counter
        
        return recursive_decode(s, 0)

# Example usage
solution = Solution()
print(solution.numDecodings("12"))     # Output: 2
print(solution.numDecodings("226"))    # Output: 3
print(solution.numDecodings("0"))      # Output: 0
print(solution.numDecodings("11111"))  # Output: 8
print(solution.numDecodings("111111111111111111111111111111111111111111111"))    # == 1836311903