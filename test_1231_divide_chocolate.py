from code_1231_divide_chocolate import Solution

def test_example_1():
    s = Solution()
    sweetness = [1,2,3,4,5,6,7,8,9]
    k = 5
    output = 6
    assert s.maximizeSweetness(sweetness, k) == output

def test_example_2():
    s = Solution()
    sweetness = [5,6,7,8,9,1,2,3,4]
    k = 8
    output = 1
    assert s.maximizeSweetness(sweetness, k) == output

def test_example_3():
    s = Solution()
    sweetness = [1,2,2,1,2,2,1,2,2]
    k = 2
    output = 5
    assert s.maximizeSweetness(sweetness, k) == output
