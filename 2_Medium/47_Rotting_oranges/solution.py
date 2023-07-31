from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        max_x_idx = len(grid[0])-1
        max_y_idx = len(grid)-1
        counter = 0
        rotten = set()  # set of tuples (x,y)

        def infectOrange(x:int, y:int, new_rottens:set) -> None:
            # out of border
            if (x<0) or (y<0) or (x>max_x_idx) or (y>max_y_idx):
                return
            # infect fresh orange
            if (grid[y][x]==1):
                grid[y][x]=2
                new_rottens.add((x,y))
                return
            return
        
        # infect neighboors of rotten oranges and update set of rotten
        # oranges to new fresly rotten oranges
        def infectNeighboors() -> None:
            nonlocal rotten
            new_rottens = set()
            for each in rotten:
                infectOrange(each[0]-1,each[1], new_rottens)
                infectOrange(each[0]+1,each[1], new_rottens)
                infectOrange(each[0],each[1]-1, new_rottens)
                infectOrange(each[0],each[1]+1, new_rottens)
            rotten = new_rottens

        # create a set of tuples with coordinates of rotten oranges (x,y)
        def find_rotten() -> None:
            for y in range(len(grid)):
                for x in range(len(grid[0])):
                    if grid[y][x] == 2 and (x,y) not in rotten:
                        rotten.add((x,y))
        
        def find_fresh() -> bool:
            for y in range(len(grid)):
                for x in range(len(grid[0])):
                    if grid[y][x] == 1:
                        return True
            return False
            
        find_rotten()
        while rotten:
            counter += 1
            infectNeighboors()
        if find_fresh() == True:
            return -1
        else:
            if counter ==0:
                return 0
        return counter-1
        

s = Solution()
print(s.orangesRotting([[2,1,1],
                        [1,1,0],
                        [0,1,1]]))

print(s.orangesRotting([[2,1,1],
                        [0,0,1],
                        [1,1,1],
                        [1,0,0],
                        [1,1,1],
                        [1,1,1]]))

print(s.orangesRotting([[0,2]]))

print(s.orangesRotting([[2,1,1],
                        [0,1,0],
                        [1,0,1]]))

print(s.orangesRotting([[0,0,0],
                        [0,0,0],
                        [0,0,0]]))