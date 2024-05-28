from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k:int) -> List[List[int]]:
        # map idx and distance into dictionary
        distance = dict({idx: x[0]*x[0]+x[1]*x[1] for idx,x in enumerate(points)})
        # sort dict according to distance
        distance = dict(sorted(distance.items(), key=lambda item: item[1]))
        return [points[k] for k in list(distance.keys())[:k]]

sol = Solution()
sol.kClosest([[3,3],[5,-1],[-2,4]], 2)
sol.kClosest([[1,3],[-2,2]], 1)
sol.kClosest([[10000,10000],[-2,2]], 1)