from solution import Solution

def test_digits1():
    s = Solution()
    assert s.letterCombinations('23') == ["ad","ae","af","bd","be","bf","cd","ce","cf"]

def test_digits2():
    s = Solution()
    assert s.letterCombinations('') == []

def test_digits3():
    s = Solution()
    assert s.letterCombinations('2') == ["a","b","c"]

def test_digits4():
    s = Solution()
    assert s.letterCombinations('234') == ['adg', 'adh', 'adi', 'aeg', 'aeh', 'aei', 'afg', 'afh', 'afi', 'bdg', 'bdh', 'bdi', 'beg', 'beh', 'bei', 'bfg', 'bfh', 'bfi', 'cdg', 'cdh', 'cdi', 'ceg', 'ceh', 'cei', 'cfg', 'cfh', 'cfi']