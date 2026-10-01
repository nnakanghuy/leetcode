class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        maxS = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1]>h:
                index, height = stack.pop()
                maxS = max(maxS, height*(i-index))
                start = index
            stack.append((start, h))
        for i, h in stack:
            maxS = max(maxS, h*(len(heights)-i))
        return maxS