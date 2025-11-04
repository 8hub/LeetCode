class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        return s == s[::-1]
    

if __name__ == "__main__":
    sol = Solution()

    assert sol.isPalindrome("A man, a plan, a canal: Panama") == True, "Test 1 Failed"
    assert sol.isPalindrome("race a car") == False, "Test 2 Failed"
    assert sol.isPalindrome(" ") == True, "Test 3 Failed"
    assert sol.isPalindrome("12321") == True, "Test 4 Failed"
    assert sol.isPalindrome("ab2a") == False, "Test 5 Failed"
    
    print("All tests passed!")