class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, subset):
            # base case. if i >= len(nums)
            if i >= len(nums):
                # add the current subset to res
                res.append(subset.copy())
                return
            
            dfs(i+1, subset)

            subset.append(nums[i])
            dfs(i+1, subset)
            subset.pop()
    
        dfs(0, [])
        return(res)