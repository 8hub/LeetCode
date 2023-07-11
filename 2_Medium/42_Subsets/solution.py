from typing import List
'''
Basic procedural parameters of backtracking algorithm:
1.  root(P): return the partial candidate at the root of the search tree.
2.  reject(P,c): return true only if the partial candidate c is not worth completing.
3.  accept(P,c): return true if c is a solution of P, and false otherwise.
4.  first(P,c): generate the first extension of candidate c.
5.  next(P,s): generate the next alternative extension of a candidate, after the extension s.
6.  output(P,c): use the solution c of P, as appropriate to the application.

In the following solution with dfs() the answer is for seperate recursive calls:
1   split:                      with element idx[0] OR without any element
2.1 split with idx[0]:          with element idx[1] OR without element idx[1]
2.2 split without any element:  with element idx[1] OR without element idx[1]
2.1.1. ----||----                      similar with OR without element idx[2]
2.1.2. ----||----                      similar with OR without element idx[2]
2.2.1. ----||----                      similar with OR without element idx[2]
2.2.2. ----||----                      similar with OR without element idx[2]
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # ans = [[]]
        # def backtrack(each):
        #     for idx in range(len(ans)):
        #         if ans[idx]==[]:
        #             ans.append([each])
        #         else:
        #             temp = ans[idx].copy()
        #             temp.append(each)
        #             ans.append(temp)
        # for each in nums:
        #     backtrack(each)
        # return ans

        ans = []
        subset = []
        def dfs(i):
            #if it is the last iteration add the result array to answer
            if i >= len(nums):
                ans.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return ans
            
s = Solution()
print(s.subsets([1,2]))
print(s.subsets([1,2,3]))