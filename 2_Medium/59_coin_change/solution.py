from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        checked = {}

        def recursive_check(amount: int):
            if amount in checked:
                return checked[amount]
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')
            
            minimal_coins = float('inf')
            
            for coin in coins:
                result = recursive_check(amount-coin)
                if result != float('inf'):
                    minimal_coins = min(minimal_coins, result+1)
                    # not always picking the biggest coin result in optimal solution
                    # bcs of that below code is wrong
                    # if minimal_coins == result + 1:
                    #     checked[amount] = minimal_coins
                    #     break

            
            checked[amount] = minimal_coins
            return minimal_coins

        result = recursive_check(amount)
        return (-1 if result == float('inf') else result)

        
sol = Solution()
print(sol.coinChange([1,2,5], 11)) # 3
print(sol.coinChange([2], 3)) # -1
print(sol.coinChange([1], 0)) # 0
print(sol.coinChange([1], 1)) # 1
print(sol.coinChange([1], 2)) # 2
print(sol.coinChange([1,2,5], 100)) # 20
print(sol.coinChange([186,419,83,408], 6249)) # 20