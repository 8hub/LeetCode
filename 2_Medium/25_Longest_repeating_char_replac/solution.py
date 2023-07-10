class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        elem_ctr = {}
        l_ptr = 0
        r_ptr = 0
        longest_replace = 0
        while(r_ptr < len(s)):
            #1 add r_ptr++
            elem_ctr[s[r_ptr]] = elem_ctr.get(s[r_ptr], 0) + 1

            #2 check if sum of not most freqent elements <= k, if yes UPDATE longest_replace
            if (sum(list(sorted(elem_ctr.values(),reverse=True)[1:])) <= k):
                longest_replace = max(longest_replace, (r_ptr-l_ptr+1))
        
            #3 if sum >k l_ptr++
            while(sum(list(sorted(elem_ctr.values(),reverse=True)[1:])) > k):
                elem_ctr[s[l_ptr]] = elem_ctr.get(s[l_ptr]) - 1
                l_ptr += 1
            r_ptr += 1
            # if r_ptr < len(s) and elem_ctr and s[r_ptr] == list(sorted(elem_ctr.items(),key=lambda x:x[1], reverse=True))[0][0]:
            #     elem_ctr[s[r_ptr]] = elem_ctr.get(s[r_ptr], 0) + 1
            #     r_ptr += 1
            # elif sum(list(sorted(elem_ctr.values(),reverse=True)[1:])) < k:
            #     elem_ctr[s[r_ptr]] = elem_ctr.get(s[r_ptr], 0) + 1
            #     r_ptr += 1
            # else:
            #     elem_ctr[s[l_ptr]] = elem_ctr.get(s[l_ptr]) - 1
            #     if elem_ctr[s[l_ptr]] == 0:
            #         del elem_ctr[s[l_ptr]]
            #     l_ptr += 1
            # longest_replace = max(longest_replace, r_ptr-l_ptr)
            
        return longest_replace

        # start_ptr = 0
        # while (start_ptr+1<len(s)) and s[start_ptr] == s[start_ptr+1] and start_ptr+1 < k:
        #     start_ptr += 1
        # end_ptr = start_ptr+1
        # if s[end_ptr] != s[start_ptr] and start_ptr+1 <= k:
        #     while(end_ptr+1<len(s)) and (s[end_ptr] == s[end_ptr+1]):
        #         end_ptr += 1
        #     longest_replace = max(longest_replace, end_ptr + 1)

s = Solution()
print(s.characterReplacement("ABAB", 2))
print(s.characterReplacement("AABABBA", 1))
print(s.characterReplacement("BAAAAABAAABAAAA", 2)) #14
print(s.characterReplacement("BAAAAABAAAB", 2))
print(s.characterReplacement("AABAAA", 1))
print(s.characterReplacement("AAAAAB", 1))
print(s.characterReplacement("BAAAAA", 1)) 
print(s.characterReplacement("BBAAAA", 2)) 
print(s.characterReplacement("BBBAAAA", 3))
print(s.characterReplacement("BBABABABAAAAA", 5))  #here is problem