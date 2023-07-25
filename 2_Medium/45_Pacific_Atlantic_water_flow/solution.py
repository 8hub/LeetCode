from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        connected_atlantic = set()
        connected_pacific = set()

        def goToAtlantic(r: int, c: int, prev: int) -> None:
            if (r < 0) or (c < 0) or (r == len(heights)) or (c == len(heights[0])) or (heights[r][c] < prev) or ((r,c) in connected_atlantic):
                return
            connected_atlantic.add((r,c))
            goToAtlantic(r-1, c, heights[r][c])     # UP
            goToAtlantic(r, c-1, heights[r][c])     # LEFT
            goToAtlantic(r+1, c, heights[r][c])     # DOWN
            goToAtlantic(r, c+1, heights[r][c])     # RIGHT

            
        def goToPacific(r: int, c: int, prev: int) -> None:
            if (r < 0) or (c < 0) or (r == len(heights)) or (c == len(heights[0])) or (heights[r][c] < prev)or ((r,c) in connected_pacific):
                return
            connected_pacific.add((r,c))
            goToPacific(r-1, c, heights[r][c])     # UP
            goToPacific(r, c-1, heights[r][c])     # LEFT
            goToPacific(r+1, c, heights[r][c])     # DOWN
            goToPacific(r, c+1, heights[r][c])     # RIGHT
        
        def search():
            # Horizontal check of connection to the Oceans
            for r in range(len(heights)):
                goToPacific(r, 0, heights[r][0])
                goToAtlantic(r, len(heights[0])-1, heights[r][len(heights[0])-1])

            # Vertical check of connection to the Oceans
            for c in range(len(heights[0])):
                goToPacific(0, c, heights[0][c])
                goToAtlantic(len(heights)-1, c, heights[len(heights)-1][c])

        search()
        answer = []
        for each in connected_atlantic:
            if each in connected_pacific:
                answer.append([each[0], each[1]])
            
        return answer
    
s = Solution()
print(s.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))