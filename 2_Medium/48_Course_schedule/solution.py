from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''if there is a loop in the prerequisites       -> return false
        because there is no way to complete 
        if numCourses > unique elements in prerequisites -> return false'''
        if len(prerequisites) == 0:
            return True
        # Create a space for graph 
        graph = {pre:[] for pre in range(numCourses)}
        # Make hashmap with all pre-courses linked to -> list [postcourses]
        for post, pre in prerequisites:
            if (post == pre):
                return False
            graph[post].append(pre)
        
        visited = set()


        def check_nodes(node):
            # loop
            if node in visited:
                return False
            # end of graph
            if graph[node] == []:
                return True
            
            visited.add(node)
            
            
            for each in graph[node]:
                if not check_nodes(each):
                    return False
            visited.remove(node)
            graph[node]=[]
            return True

        for course in range(numCourses):
            if not check_nodes(course):
                return False
        return True
            
            







s = Solution()
print(s.canFinish(4, [[2,0],[1,0],[3,1],[3,2],[1,3]]))      # false
print(s.canFinish(2, [[1,0]]))                              # true
print(s.canFinish(2, [[1,0], [0,1]]))                       # false
print(s.canFinish(3, [[1,0], [2,1]]))                       # true
print(s.canFinish(4, [[1,0], [2,1], [3,2]]))                # true
print(s.canFinish(5, [[1,0], [2,1], [3,2], [4,3], [4,0]]))  # true
print(s.canFinish(5, [[1,0], [2,1], [3,2], [4,3], [0,4]]))  # true
print(s.canFinish(3, [[0,1], [1,2], [2,0]]))                # false
print(s.canFinish(4, [[0,1], [1,2], [2,3], [3,0]]))         # false
print(s.canFinish(2, [[0,1]]))                              # true
print(s.canFinish(1, []))                                   # true
print(s.canFinish(6, [[1,0], [2,0], [3,1], [4,3], [5,4]]))  # true
print(s.canFinish(5, [[1,0], [2,0], [3,1], [4,1]]))         # true
print(s.canFinish(20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]))  # false