from solution import Solution

def test1() ->None:
    s = Solution()
    assert s.containsDuplicate([1,2,3,1]) == True

def test2() ->None:
    s = Solution()
    assert s.containsDuplicate([1,2,3,4]) == False
    
def test3() ->None:
    s = Solution()
    assert s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True