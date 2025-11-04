class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        solution = [0] * (len(num1) + len(num2))
        for i1, number_num1 in enumerate(num1[::-1]):
            number_num1 = int(number_num1)
            for i2, number_num2 in enumerate(num2[::-1], i1):
                number_num2 = int(number_num2)
                curr_result = number_num1 * number_num2
                solution[i2] += curr_result % 10
                solution[i2+1] += curr_result // 10
                
                if solution[i2] >= 10:
                    solution[i2+1] += solution[i2] // 10
                    solution[i2] %= 10

        return ''.join(map(str, solution[::-1])).lstrip('0')




if __name__ == "__main__":
    sol = Solution()

    # Test 1: Basic single digits
    assert sol.multiply("2", "3") == "6", "Test 1 Failed"

    # Test 2: Larger numbers (example from problem)
    assert sol.multiply("123", "456") == "56088", "Test 2 Failed"

    # Test 3: One number is zero
    assert sol.multiply("0", "12345") == "0", "Test 3 Failed"
    assert sol.multiply("12345", "0") == "0", "Test 4 Failed"

    # Test 4: Both numbers are zero
    assert sol.multiply("0", "0") == "0", "Test 5 Failed"

    # Test 5: Single digit with multi-digit
    assert sol.multiply("9", "99") == "891", "Test 6 Failed"
    assert sol.multiply("99", "9") == "891", "Test 7 Failed"

    # Test 6: Numbers with leading zeros (but valid since non-negative strings)
    assert sol.multiply("10", "10") == "100", "Test 8 Failed"

    # Test 7: Large product (no overflow in string)
    assert sol.multiply("999", "999") == "998001", "Test 9 Failed"

    # Test 8: One-digit and two-digit
    assert sol.multiply("5", "12") == "60", "Test 10 Failed"

    # Test 9: Very large input strings (edge case for manual multiplication)
    assert sol.multiply("888", "888") == "788544", "Test 11 Failed"

    # Test 10: Minimal valid input
    assert sol.multiply("1", "1") == "1", "Test 12 Failed"

    print("All tests passed!")