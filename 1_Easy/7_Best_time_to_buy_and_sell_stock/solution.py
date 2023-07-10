from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        len_prices = len(prices)
        if len_prices==1:
            return 0
        r = 1
        max_diff = 0
        while (r<len_prices):
            while(l+1 < len_prices) and (prices[l]>= prices[l+1]):
                l += 1
            r = l + 1
            while(r < len_prices) and (prices[r] >= prices[l]):
                if (prices[r] - prices[l] > max_diff):
                    max_diff = (prices[r] - prices[l])
                r += 1
            l = r
        return max_diff

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([7,6,4,3,1]))
print(s.maxProfit([7]))
print(s.maxProfit([7,8]))