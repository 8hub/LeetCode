from solution import Solution

def test_longest_palindrome():
    s = Solution()
    assert s.longestPalindrome('labar') == 'aba'

def test_longest_palindrome2():
    s = Solution()
    assert s.longestPalindrome('lliabar') == 'aba'
    
def test_longest_palindrome3():
    s = Solution()
    assert s.longestPalindrome('labal') == 'labal'
    
def test_longest_palindrome4():
    s = Solution()
    assert s.longestPalindrome('xabaxtd') == 'xabax'
    
def test_longest_palindrome5():
    s = Solution()
    assert s.longestPalindrome('x') == 'x'
    
def test_longest_palindrome6():
    s = Solution()
    assert s.longestPalindrome('xbx') == 'xbx'

def test_longest_palindrome7():
    s = Solution()
    assert s.longestPalindrome('lcbbcr') == 'cbbc'

def test_longest_palindrome8():
    s = Solution()
    assert s.longestPalindrome('slowo') == 'owo'
    
def test_longest_palindrome9():
    s = Solution()
    assert s.longestPalindrome('babad') == 'bab'

def test_longest_palindrome10():
    s = Solution()
    assert s.longestPalindrome('a') == 'a'

def test_longest_palindrome11():
    s = Solution()
    assert s.longestPalindrome('bb') == 'bb'
    
def test_longest_palindrome12():
    s = Solution()
    assert s.longestPalindrome('aleb') == 'a'
        
def test_longest_palindrome13():
    s = Solution()
    assert s.longestPalindrome('aaaaaa') == 'aaaaaa'
    
def test_longest_palindrome14():
    s = Solution()
    assert s.longestPalindrome('reifadyqgztixemwswtccodfnchcovrmiooffbbijkecuvlvukecutasfxqcqygltrogrdxlrslbnzktlanycgtniprjlospzhhgdrqcwlukbpsrumxguskubokxcmswjnssbkutdhppsdckuckcbwbxpmcmdicfjxaanoxndlfpqwneytatcbyjmimyawevmgirunvmdvxwdjbiqszwhfhjmrpexfwrbzkipxfowcbqjckaotmmgkrbjvhihgwuszdrdiijkgjoljjdubcbowvxslctleblfmdzmvdkqdxtiylabrwaccikkpnpsgcotxoggdydqnuogmxttcycjorzrtwtcchxrbbknfmxnonbhgbjjypqhbftceduxgrnaswtbytrhuiqnxkivevhprcvhggugrmmxolvfzwadlnzdwbtqbaveoongezoymdrhywxcxvggsewsxckucmncbrljskgsgtehortuvbtrsfisyewchxlmxqccoplhlzwutoqoctgfnrzhqctxaqacmirrqdwsbdpqttmyrmxxawgtjzqjgffqwlxqxwxrkgtzqkgdulbxmfcvxcwoswystiyittdjaqvaijwscqobqlhskhvoktksvmguzfankdigqlegrxxqpoitdtykfltohnzrcgmlnhddcfmawiriiiblwrttveedkxzzagdzpwvriuctvtrvdpqzcdnrkgcnpwjlraaaaskgguxzljktqvzzmruqqslutiipladbcxdwxhmvevsjrdkhdpxcyjkidkoznuagshnvccnkyeflpyjzlcbmhbytxnfzcrnmkyknbmtzwtaceajmnuyjblmdlbjdjxctvqcoqkbaszvrqvjgzdqpvmucerumskjrwhywjkwgligkectzboqbanrsvynxscpxqxtqhthdytfvhzjdcxgckvgfbldsfzxqdozxicrwqyprgnadfxsionkzzegmeynye') == 'uvlvu'
    
def test_longest_palindrome1():
    s = Solution()
    assert s.longestPalindrome('aavlvuvllvux') == 'uvllvu'

def test_even_paindrome_from_pos0():
    s = Solution()
    assert s.longestEvenPalindrome('labbar',2) == 'abba'
    
def test_even_paindrome_from_pos1():
    s = Solution()
    assert s.longestEvenPalindrome('labbar',3) == ''
    
def test_even_paindrome_from_pos2():
    s = Solution()
    assert s.longestEvenPalindrome('labbal',2) == 'labbal'
    
def test_odd_paindrome_from_pos0():
    s = Solution()
    assert s.longestOddPalindrome('labar',2) == 'aba'
    
def test_odd_paindrome_from_pos1():
    s = Solution()
    assert s.longestOddPalindrome('labar',3) == 'a'
    
def test_odd_paindrome_from_pos2():
    s = Solution()
    assert s.longestOddPalindrome('labal',2) == 'labal'