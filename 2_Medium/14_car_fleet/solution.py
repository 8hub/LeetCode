from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_nr = len(position)
        #pair of i-th car position and time to get to the destination
        fleets = [[position[i],(target-position[i])/speed[i]] for i in range(car_nr)]
        #sort according to position
        fleets = sorted(fleets,key=lambda x:x[0], reverse=True)
        stack = [fleets[0][1]]
        for index, fleet in enumerate(fleets):
            if (fleet[1] <= stack[-1]):
                continue
            else:
                stack.append(fleet[1])
        return len(stack)

s = Solution()
print(s.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))
print(s.carFleet(10, [3], [3]))
print(s.carFleet(100, [0,2,4], [4,2,1]))