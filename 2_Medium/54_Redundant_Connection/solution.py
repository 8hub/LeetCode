from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

# The find function is a helper function used to find the root of a node.
# It uses path compression, which means that as it finds the root,
# it updates the parent of each node along the path to point
# directly to the root. This helps to flatten the tree and speed up
# future queries.
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        for edge in edges:
            x, y = edge
            if find(x) == find(y):
                return edge
            elif rank[x] >= rank[y]:
                parents[find(y)] = find(x)
                rank[x] += 1
            else:
                parents[find(x)] = find(y)
                rank[y] += 1
        return None

sol = Solution()
print(sol.findRedundantConnection([[1,2],[1,3],[2,3]]))  # Output: [2, 3]
print(sol.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))  # Output: [1, 4]
print(sol.findRedundantConnection([[3,4],[1,2],[2,4],[3,5],[2,5]]))  # Output: [2, 5]
print(sol.findRedundantConnection([[3,4],[1,2],[2,4],[3,5],[4,1]]))  # Output: [4, 1]