class Solution:
    #    Input: s = "PAYPALISHIRING", numRows = 4
    #    Output: "PINALSIGYAHRPI"
    #    Explanation:
    #   (0)   (1)   (2)
    #    P     I     N
    #    A   L S   I G
    #    Y A   H R
    #    P     I
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        arr = [[] for _ in range(numRows)]
        cross_nr = 1
        # col_nr = 0
        # row_nr = 0
        doCross = False
        for idx, ch in enumerate(s):
            # create each vertical full of chars column
            if (idx%(numRows+numRows-2) < numRows) and (not doCross):
                arr[idx%(numRows+numRows-2)].append(ch)
                if idx%(numRows+numRows-2) == numRows-1:
                    doCross = True
            # create a cross part
            if doCross and (idx%(numRows+numRows-2) > numRows-1):
                for each in range(numRows):
                    if each == (numRows-1)-cross_nr:
                        arr[each].append(ch)
                    else:
                        arr[each].append(" ")
                cross_nr += 1
            if doCross and cross_nr > numRows-2:
                doCross = False
                cross_nr = 1
        ans = ""
        for each in arr:
            for char in each:
                if char != ' ':
                    ans = ans+char
        return ans
    

sol = Solution()
print(sol.convert("PAYPALISHIRING", 2))
print(sol.convert("PAYPALISHIRING", 3))
print(sol.convert("PAYPALISHIRING", 4))