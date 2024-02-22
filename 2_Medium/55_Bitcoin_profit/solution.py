class Solution():
    def check_profit(self, arr: list[int]):
        if arr == []:
            return None
        curr_min = arr[0]
        curr_max = arr[0]
        max_diff = 0
        for each in arr:
            if each < curr_min:
                curr_min = each
                curr_max = each
            elif each > curr_max:
                curr_max = each
            max_diff = max(max_diff, curr_max - curr_min)
        return max_diff

solution = Solution()
print(solution.check_profit([7,1,5,3,6,4]))
print(solution.check_profit([8,5,4,2]))
print(solution.check_profit([8,5,4,2,4,5,6,1,2,4,7]))
print(solution.check_profit([]))