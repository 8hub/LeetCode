class Solution:
    def longestOddPalindrome(self, s: str, center_position: int) -> str:
        curr_subpalindrome = s[center_position]
        iteration = 0
        #       'labar'
        #        012345
        still_palindrome = 1
        while (center_position - iteration) >= 0 and (center_position + iteration) < len(s) and still_palindrome == 1:
            still_palindrome = 0
            if (s[center_position - iteration] == s[center_position + iteration]):
                curr_subpalindrome = s[center_position - iteration:center_position + iteration+1]
                still_palindrome = 1
            iteration += 1
        return curr_subpalindrome

# To change. For now it is the same as odd method
    def longestEvenPalindrome(self, s: str, center_position_l: int) -> str:
        curr_subpalindrome = ''
        iteration = 0
        #       'labbar'
        #        012345
        still_palindrome = 1
        # First to check -1 index and +1 index and if the letter is the
        # same add it to the subpalindrome and search further
        while (center_position_l - iteration) >= 0 and (center_position_l + iteration+1) < len(s) and still_palindrome == 1:
            still_palindrome = 0
            if (s[center_position_l - iteration] == s[center_position_l + iteration+1]):
                curr_subpalindrome = s[center_position_l - iteration:center_position_l + iteration+2]
                still_palindrome = 1
            iteration += 1
        return curr_subpalindrome
    
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ''
        for i in range(len(s)):
            curr_subpalindrome = '' #even subpalindrome
            curr_subpalindrome_odd = self.longestOddPalindrome(s,i)
            if(i+1 < len(s) and s[i] == s[i+1]):
                curr_subpalindrome = self.longestEvenPalindrome(s,i)
            if (len(curr_subpalindrome) < len(curr_subpalindrome_odd)):
                curr_subpalindrome = curr_subpalindrome_odd
            if (len(longest_palindrome) < len(curr_subpalindrome)):
                longest_palindrome = curr_subpalindrome
        return longest_palindrome
                

    def isPalindrome(self, sub: str) -> bool:
        return sub == sub[::-1]
    
    ### Work, but time complexity is to high: O(N^3)
    # def longestPalindrome(self, s: str) -> str:
    #     longest_palindrome = ''
    #     for i in range(len(s)):
    #         for j in range (i,len(s)):
    #             curr_subpalindrome = ''
    #             if (self.isPalindrome(s[i:j+1])):
    #                 curr_subpalindrome = s[i:j+1]
    #                 if(len(longest_palindrome) < len(curr_subpalindrome)):
    #                    longest_palindrome = curr_subpalindrome
    #     return longest_palindrome