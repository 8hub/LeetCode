from solution import Solution

def test_twoSum1():
    s = Solution()
    assert s.twoSum([2, 7, 11 ,15], 9) == [0, 1]
    
def test_twoSum2():
    s = Solution()
    assert s.twoSum([2, 7, 11 ,15], 22) == [1, 3]
        
def test_twoSum3():
    s = Solution()
    assert s.twoSum([3, 2, 4], 6) == [1, 2]
        
def test_twoSum4():
    s = Solution()
    assert s.twoSum([3, 3], 6) == [0, 1] or [1, 0]