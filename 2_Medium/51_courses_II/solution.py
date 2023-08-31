from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {pre:[] for pre in range(numCourses)}
        [graph[course].append(pre) for course, pre in prerequisites]

        visited = set()
        cycle = set()
        sorted = []
    
        def dfs(node):
            if node in cycle:
                return False
            if node in visited:
                return True
            cycle.add(node)
            for each in graph[node]:
                if dfs(each) == False:
                    return False
            visited.add(node)
            cycle.remove(node)
            sorted.append(node)
            return True

        for each in range(numCourses):
            if dfs(each) == False:
                return []
        return sorted

    
# Here is explanation in steps how the algorithm works:
# 1. Build graph based on prerequisites
# 2. Iterate through graph nodes
# 3. For each node do dfs
# 4. If dfs returns False it means that there is a cycle
# 5. If dfs returns True it means that there is no cycle
# 6. Return output which will contain topological order of graph nodes

s = Solution()
print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))            # [0,1,2,3] or [0,2,1,3]
print(s.findOrder(2, [[1,0]]))                              # [0,1]
print(s.findOrder(2, [[1,0], [0,1]]))                       # []
print(s.findOrder(3, [[1,0], [2,1]]))                       # [0,1,2]
print(s.findOrder(4, [[1,0], [2,1], [3,2]]))                # [0,1,2,3]
print(s.findOrder(5, [[1,0], [3,1], [2,1], [4,2]]))         # [0,1,2,3,4]