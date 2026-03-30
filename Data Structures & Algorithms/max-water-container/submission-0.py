class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l, r = 0, len(heights) - 1
        while l < r:
            cArea = (r - l) * min(heights[l], heights[r])
            maxArea = max(maxArea, cArea)
            if heights[r] <= heights[l]:
                r -= 1
            else:
                l += 1
        return(maxArea)

                
            