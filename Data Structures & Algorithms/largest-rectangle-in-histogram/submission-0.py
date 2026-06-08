class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i, h in enumerate(heights):
            popI = i
            while stack and stack[-1][1] > h:
                popI, popH = stack.pop()
                area = popH * (i - popI)
                maxArea = max(maxArea, area)
            stack.append([popI, h])
        
        for i, h in stack:
            area = (len(heights) - i) * h
            maxArea = max(maxArea, area)
        
        return maxArea