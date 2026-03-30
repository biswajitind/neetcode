class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # we can extend towards left and right.
        # we stop extending towards right as soon as we find that the next one's height is less.
        #    This is the point we will compute
        # while computing we will take in to consideration the left as well.

        # in other words, we will use a stack and keep pushin into the stack as long as the next
        # one's height is greater.
        # we will also store the index of the heights in the stack.

        maxArea = 0
        stack = []
        for idx, height in enumerate(heights):
            if stack and stack[-1][0] <= height:
                stack.append([height, idx])
                continue
            newIdx = idx
            while stack and stack[-1][0] > height:
                prev = stack.pop()
                newIdx = prev[1]
                area = prev[0] * (idx - prev[1])
                maxArea = max(maxArea, area)
            stack.append([height, newIdx])
        
        # now lets check the reminder of the stack.
        while stack:
            entry = stack.pop()
            area = entry[0] * ( len(heights) - entry[1])
            maxArea = max(maxArea, area)
        #print(stack)
        return(maxArea)





