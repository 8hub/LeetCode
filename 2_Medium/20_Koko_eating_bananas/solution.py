import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles = sorted(piles)
        last_idx = len(piles)-1
        lp = math.ceil(sum(piles)/h)
        rp = piles[last_idx]
        ans = 0
        def time_for_speed(k):
            hours_of_eating = 0
            pile_idx = 0
            while hours_of_eating <= h and pile_idx <= last_idx:
                hours_of_eating += (piles[pile_idx]//k + (1 if piles[pile_idx]%k > 0 else 0))
                pile_idx += 1
            return hours_of_eating
        while(lp <= rp):
            mid = (lp+rp)//2
            #when the eating time is to long Koko has to eat faster
            if(time_for_speed(mid)>h):
                lp = mid+1
            #when the eating time is to short Koko has to eat slower
            else:
                ans = mid
                rp = mid - 1
        return ans


        
s = Solution()
print(s.minEatingSpeed([3,6,7,11],8))       #4
print(s.minEatingSpeed([1,6,9,11],8))       #5
print(s.minEatingSpeed([30,11,23,4,20],5))  #30
print(s.minEatingSpeed([30,11,23,4,20],6))  #23
print(s.minEatingSpeed([30,23,20,11,4],7))  #20
print(s.minEatingSpeed([30,23,20,11,4],8))  #15
print(s.minEatingSpeed([312884470],312884469))             #2